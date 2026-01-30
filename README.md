# codealpha_portfolio-tracker

---

# Stock Portfolio Tracker (Python)

This is a simple **command-line Stock Portfolio Tracker** written in Python.  
It allows users to enter stock symbols and quantities, calculate the total investment value, and optionally save the portfolio to a file.

---

## Features

- Predefined stock prices
- User input validation
- Calculates individual stock values
- Displays total portfolio value
- Option to save portfolio details to a text file

---

## Stock Prices Used

The program uses the following fixed stock prices:

| Stock | Price ($) |
|------|-----------|
| AAPL | 180 |
| TSLA | 250 |
| GOOG | 2700 |
| MSFT | 330 |

---

## How the Program Works

1. The user enters a stock symbol
2. The program checks if the symbol is valid
3. The user enters the quantity of shares
4. The program calculates:
   - Value of each stock
   - Total investment value
5. The user can choose to save the results to a file

---

## Example Output

AAPL: 2 x $180 = $360
TSLA: 1 x $250 = $250
Total investment value: $610

---

## How to Run the Program

1. Make sure Python 3 is installed
2. Open a terminal in the project folder
3. Run the program:

portfolio tracker.py
4.	Follow the on-screen prompts to enter stocks and quantities

---

Saving to a File
•	After calculations, the program asks if you want to save the portfolio
•	If you choose yes, enter a filename (e.g., portfolio.txt)
•	The file will include:
o	Stock details
o	Quantities
o	Individual values
o	Total investment value

---

Error Handling
•	Invalid stock symbols are rejected
•	Quantity must be a positive number
•	Non-numeric input is handled safely
•	File-saving errors are caught and displayed

---

Technologies Used
Language: Python Tool: VS Code

---

Author
Komal Bagal
