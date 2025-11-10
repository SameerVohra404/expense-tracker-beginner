# 🧾 Expense Tracker (Beginner Python Project)

A simple command-line **Expense Tracker** written in Python that allows users to record and manage daily expenses.  
It focuses on learning input validation, error handling, data structures, and loops — perfect for Python beginners.

---

## 🚀 Features

- Add new expenses with the following details:
  - **Date** – Auto-fills with today’s date if left blank.  
  - **Category** – Rejects any numeric input.  
  - **Amount** – Accepts only numbers greater than 0; handles invalid input gracefully.  
  - **Description** – Optional short note about the expense.  
- Stores all expenses in a list (`expense_db`) until the program exits.  
- Displays all stored expenses in a clean, readable format after each entry.  
- Prevents program crashes using `try/except` blocks for validation.  

---

## 🧠 What You’ll Learn

This project helps you practice:

- Python **dictionaries** and **lists**
- **Loops** and **input handling**
- **try/except** error handling
- Working with **dates** using the `datetime` module
- Structuring and validating user input

---

## ⚙️ How It Works

1. The script starts an infinite loop (`while True`) to continuously take user input.  
2. It stores each expense in a **dictionary**.  
3. Each dictionary is appended to a **list** (`expense_db`), acting as a temporary in-memory database.  
4. When the user chooses not to continue, the program stops but retains all data from the current session (until the script ends).  

---

## 🧰 Technologies Used

- **Python 3.10+**
- Built-in modules only (`datetime`)

---

## 💡 Future Improvements

Planned features for next versions:

- ✅ Update or delete an existing expense  
- 📊 View total and average spending  
- 💾 Save and load expenses from a file (CSV or JSON)  
- 🧮 Generate monthly or category-based reports  
- 🖥️ Add a menu system for easier navigation  

---

## 👨‍💻 Author

**Sameer Vohra**  
Student | Python & AI Enthusiast | GBS Dubai  
*(Created as part of my journey to strengthen Python fundamentals.)*
