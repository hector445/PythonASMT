import easygui
import pandas as pd
import matplotlib.pyplot as plt
import csv

#Collect user details
name = easygui.enterbox("Enter your name:")
job = easygui.enterbox("Enter your profession:")
salary = easygui.enterbox("Enter your net pay ($):")

#Expense categories
categories = ["Rent", "Utilities", "Groceries", "EatingOut", "Entertainment", "Petrol", "Other"]
expenses = []  #List to store expenses

def save_to_csv():
    with open("expenses.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Amount"])
        writer.writerows(expenses)

def show_graph():
    if not expenses:
        easygui.msgbox("No expenses recorded.")
        return
    
    df = pd.DataFrame(expenses, columns=["Category", "Amount"])
    df_grouped = df.groupby("Category")["Amount"].sum()
    
    df_grouped.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.xlabel("Categories")
    plt.ylabel("Amount ($)")
    plt.title("Spending Chart")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

#Main loop
while True:
    choice = easygui.buttonbox("Choose an option:", choices=["Add Expense", "Summary", "Graph", "Exit"])

    if choice == "Add Expense":
        category = easygui.choicebox("Select category:", choices=categories)
        amount = easygui.enterbox("Enter amount ($):")

        if category and amount and amount.replace('.', '', 1).isdigit():
            expenses.append((category, float(amount)))
            easygui.msgbox("Expense added!")
            save_to_csv()
        else:
            easygui.msgbox("Invalid amount. Try again.")

    elif choice == "Summary":
        if not expenses:
            easygui.msgbox("No expenses recorded.")
        else:
            total_spent = sum(amount for _, amount in expenses)
            savings = float(salary) - total_spent

            summary = "\n".join([f"{cat}: ${amt:.2f}" for cat, amt in expenses])

            easygui.msgbox(f"Summary:\n\n{summary}\n\nTotal: ${total_spent:.2f}\nSavings: ${savings:.2f}")
    
    elif choice == "Graph":
        show_graph()

    else:
        break
