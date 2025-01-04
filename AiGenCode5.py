import pandas as pd
from datetime import datetime, timedelta
import random

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount, category=None):
        new_expense = {'name': name, 'amount': amount, 'category': category}
        self.expenses.append(new_expense)

    def get_average_expense_by_category(self):
        categories = {}
        for expense in self.expenses:
            if expense['category'] not in categories:
                categories[expense['category']] = []
            categories[expense['category']].append(expense['amount'])
        
        average_expenses = {category: sum(amounts) / len(amounts) for category, amounts in categories.items()}
        return average_expenses

    def get_most_expensive_month(self):
        months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 
                  'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
        
        expense_data = {}
        for expense in self.expenses:
            month = datetime.strptime(expense['date'], '%Y-%m-%d').month
            if month not in expense_data:
                expense_data[month] = []
            expense_data[month].append(expense['amount'])
        
        most_expensive_month = max(expense_data, key=lambda x: sum(expense_data[x]))
        return f"{most_expensed_month} was the most expensive month with an average expenditure of ${sum(expense_data[most_expensive_month]) / len(expense_data[most_expensive_month]):.2f}"

    def get_total_expenses_by_year(self):
        expense_data = {}
        
        for expense in self.expenses:
            year = datetime.strptime(expense['date'], '%Y-%m-%d').year
            if year not in expense_data:
                expense_data[year] = []
            expense_data[year].append(expense['amount'])
        
        total_expenses_by_year = {year: sum(amounts) for year, amounts in expense_data.items()}
        return total_expenses_by_year

# Example usage
tracker = ExpenseTracker()
tracker.add_expense('Rent', 1000)
tracker.add_expense('Groceries', 500, 'Food')
tracker.add_expense('Transportation', 200, 'Transport')
tracker.add_expense('Entertainment', 300)

print(tracker.get_average_expense_by_category())
print(tracker.get_most_expensive_month())
print(tracker.get_total_expenses_by_year())
