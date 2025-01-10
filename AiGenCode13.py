import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

# Define an enum for different types of expenses
class ExpenseType(Enum):
    FOOD = "Food"
    TRANSPORTATION = "Transportation"
    ENTERTAINMENT = "Entertainment"

# Define a data class to represent a transaction
@dataclass
class Transaction:
    date: datetime.date
    amount: float
    description: str

# Define a class to manage expenses
class ExpenseManager:
    def __init__(self):
        self.expenses: List[Transaction] = []

    # Method to add a new expense
    def add_expense(self, amount: float, description: str) -> Transaction:
        return Transaction(datetime.date.today(), amount, description)

    # Method to get all expenses by type
    def get_expenses_by_type(self, expense_type: ExpenseType) -> List[Transaction]:
        return [transaction for transaction in self.expenses if transaction.description == f"{expense_type.value}"]


# Example usage:
if __name__ == "__main__":
    manager = ExpenseManager()

    # Add some expenses
    manager.add_expense(10.99, "Coffee")
    manager.add_expense(50.00, "Monthly Transportation Fee")
    manager.add_expense(20.00, "Dinner")

    # Get all food expenses
    food_expenses = manager.get_expenses_by_type(ExpenseType.FOOD)
    print("Food Expenses:")
    for expense in food_expenses:
        print(f"Date: {expense.date}, Amount: ${expense.amount:.2f}")

    # Get all entertainment expenses
    entertainment_expenses = manager.get_expenses_by_type(ExpenseType.ENTERTAINMENT)
    print("\nEntertainment Expenses:")
    for expense in entertainment_expenses:
        print(f"Date: {expense.date}, Amount: ${expense.amount:.2f}")
