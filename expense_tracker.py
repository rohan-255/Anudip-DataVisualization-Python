#libraries
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rohan@2005",
    database="expense_tracker"
)

query = "SELECT * FROM expenses"
df = pd.read_sql(query, db)
print(df)

# calculations
total_expense = df['amount'].sum()
average_expense = df['amount'].mean()
median_expense = df['amount'].median()

print("Total Expense:", total_expense)
print("Average Expense:", average_expense)
print("Median Expense:", median_expense)

high_expenses = df[df['amount'] > average_expense]
print("\nHigh Expenses:")
print(high_expenses)

#chart (daily trend)
plt.figure()
plt.plot(df['date'], df['amount'], marker='o')
plt.xlabel("Date")
plt.ylabel("Amount")
plt.title("Daily Expense Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7. Bar chart (category-wise)
category_sum = df.groupby('category')['amount'].sum()

plt.figure()
category_sum.plot(kind='bar')
plt.xlabel("Category")
plt.ylabel("Total Expense")
plt.title("Category-wise Expense Analysis")
plt.tight_layout()
plt.show()

