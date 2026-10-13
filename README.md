# Stock Portfolio Tracker

## Project Overview

The Stock Portfolio Tracker is a simple Python application developed as part of the CodeAlpha Python Programming Internship.

The program calculates the total investment value of a stock portfolio using predefined stock prices stored in a Python dictionary. Users enter stock symbols and quantities, and the program calculates the investment value for each stock and the total portfolio value.

## Features

- Predefined stock prices stored in a dictionary.
- User input for stock symbols and quantities.
- Calculation of individual stock investment values.
- Calculation of total portfolio investment.
- Display of a portfolio summary.
- Saving portfolio details to a text file named `portfolio.txt`.

## Technologies Used

- Programming Language: Python
- Dictionary
- Loops and conditional statements
- User input and output
- Basic arithmetic operations
- File handling

## Available Stocks

The program includes the following predefined stock symbols and example prices:

| Stock Symbol | Price per Share |
|---|---:|
| AAPL | $180 |
| TSLA | $250 |
| GOOGL | $140 |
| MSFT | $420 |
| AMZN | $190 |

These prices are hardcoded examples and do not represent live market prices.

## Installation and Execution

1. Install Python on your computer.
2. Save the source code as `stock_portfolio_tracker.py`.
3. Open a terminal in the project directory.
4. Run the following command:

   ```bash
   python stock_portfolio_tracker.py
   ```

5. Enter the number of stocks you want to add.
6. Enter each stock symbol and its quantity.
7. View the investment summary in the terminal.

The program also creates `portfolio.txt` in the current working directory and saves the portfolio summary.

## Calculation Method

The investment value for each stock is calculated using the following formula:

Investment Value = Stock Price × Quantity

The total investment is calculated by adding the investment values of all valid stock entries.

## Learning Outcomes

This project provides practical experience with Python dictionaries, loops, conditional statements, user input, arithmetic operations, and file handling. It also demonstrates how Python can be used to perform basic financial calculations.

## Internship Information

Organization: CodeAlpha

Program: Python Programming Internship

Task: Task 2 - Stock Portfolio Tracker

## Project Purpose

This project was developed for educational purposes to strengthen Python programming fundamentals and apply them to a simple stock investment tracking application.
