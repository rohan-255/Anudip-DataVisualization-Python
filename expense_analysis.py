import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_excel("expenses.xlsx")

print("Expense Data:")
print(df)

total_expense = df["Amount"].sum()
print("Total Expense:", total_expense)

average_expense = df["Amount"].mean()
print("Average Expense:", average_expense)

median_expense = df["Amount"].median()
print("Median Expense:", median_expense)

high_expenses = df[df["Amount"] > average_expense]

print("\nHigh Expenses:")
print(high_expenses)

category_expense = df.groupby("Category")["Amount"].sum()
print("\nCategory-wise Expense:")
print(category_expense)

plt.figure()
plt.plot(df["Date"], df["Amount"], marker='o')
plt.xlabel("Date")
plt.ylabel("Amount")
plt.title("Expense Trend Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
category_expense.plot(kind='bar')
plt.xlabel("Category")
plt.ylabel("Total Amount")
plt.title("Category-wise Expenses")
plt.tight_layout()
plt.show()
