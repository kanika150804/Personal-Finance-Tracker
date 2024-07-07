import tkinter as tk
from tkinter import messagebox
import json

# File to store data
DATA_FILE = 'finance_data.json'

# Load data from file
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'income': [], 'expenses': [], 'savings': 0}

# Save data to file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

# Add income
def add_income():
    try:
        amount = float(income_entry.get())
        remark = income_remark_entry.get()
        data['income'].append({'amount': amount, 'remark': remark})
        data['savings'] += amount
        save_data(data)
        update_display()
        income_entry.delete(0, tk.END)
        income_remark_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount")

# Add expense
def add_expense():
    try:
        amount = float(expense_entry.get())
        remark = expense_remark_entry.get()
        data['expenses'].append({'amount': amount, 'remark': remark})
        data['savings'] -= amount
        save_data(data)
        update_display()
        expense_entry.delete(0, tk.END)
        expense_remark_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount")

# Update display
def update_display():
    income_list.delete(0, tk.END)
    for income in data['income']:
        if isinstance(income, dict):
            income_list.insert(tk.END, f'+ {income["amount"]:.2f} ({income["remark"]})')
        else:
            income_list.insert(tk.END, f'+ {income:.2f}')

    expense_list.delete(0, tk.END)
    for expense in data['expenses']:
        if isinstance(expense, dict):
            expense_list.insert(tk.END, f'- {expense["amount"]:.2f} ({expense["remark"]})')
        else:
            expense_list.insert(tk.END, f'- {expense:.2f}')

    savings_label.config(text=f'Savings: {data["savings"]:.2f}')

# Initialize data
data = load_data()

# Create the main window
root = tk.Tk()
root.title('Personal Finance Manager')

# Income section
tk.Label(root, text='Add Income:').grid(row=0, column=0)
income_entry = tk.Entry(root)
income_entry.grid(row=0, column=1)
tk.Label(root, text='Remark:').grid(row=0, column=2)
income_remark_entry = tk.Entry(root)
income_remark_entry.grid(row=0, column=3)
tk.Button(root, text='Add', command=add_income).grid(row=0, column=4)

# Expense section
tk.Label(root, text='Add Expense:').grid(row=1, column=0)
expense_entry = tk.Entry(root)
expense_entry.grid(row=1, column=1)
tk.Label(root, text='Remark:').grid(row=1, column=2)
expense_remark_entry = tk.Entry(root)
expense_remark_entry.grid(row=1, column=3)
tk.Button(root, text='Add', command=add_expense).grid(row=1, column=4)

# Income list
tk.Label(root, text='Income:').grid(row=2, column=0)
income_list = tk.Listbox(root)
income_list.grid(row=3, column=0, columnspan=5, sticky='nsew')

# Expense list
tk.Label(root, text='Expenses:').grid(row=4, column=0)
expense_list = tk.Listbox(root)
expense_list.grid(row=5, column=0, columnspan=5, sticky='nsew')

# Savings display
savings_label = tk.Label(root, text='Savings: 0.00')
savings_label.grid(row=6, column=0, columnspan=5)

# Update display with initial data
update_display()

# Run the application
root.mainloop()
