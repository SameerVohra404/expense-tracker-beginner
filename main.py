import datetime

expense_db = []



while True:
    expense = {"date":None,"category":None,"amount":None,"description":None}

    date_input = input("Enter date in YYYY-MM-DD format (press enter for today) : ")
    category = input("Enter category : ")
    amount = input("Enter amount : ")
    descr = input("Enter description : ")

    if date_input.strip() == "":
        expense["date"] = datetime.date.today()
    else:
        try:
            expense["date"] = datetime.datetime.strptime(date_input,"%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format! use YYYY-MM-DD format")
            expense["date"] = None

    if amount.strip() == "":
        expense["amount"] = "Free"
    else:
        try:
         amount = int(amount)
         if amount<1 :
          print("Invalid input amount cannot be less than 1")
          expense["amount"] = "Invalid Input"
         else:
          expense["amount"] = amount
          
        except ValueError:
           print("Invalid input : only numbers are allowed in amount")
           expense["amount"] = "Invalid Input"
    
    if category.strip() == "":
        expense["category"] = None     
    elif any(char.isdigit() for char in category): 
        print("Numbers are not allowed in category")
        expense["category"] = "Invalid Input"
    else:
        expense["category"] = category

    
    if descr.strip() == "":
        expense["description"] = None
    else:
        expense["description"] = descr     
        

    expense_db.append(expense)
    
    for e in expense_db:
        print("Date:",e["date"].strftime("%Y-%m-%d") if e["date"] else None,
              "| Category:", e["category"], "| Amount:", e["amount"], "| Description:", e["description"])

    resume = input("Do you wish to continue? y/n : ")
    if resume.lower() != "y":
        break

    