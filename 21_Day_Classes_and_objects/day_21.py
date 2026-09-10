# Exercises - Day 21

from collections import Counter
from math import sqrt


# === LEVEL 1 ===

# 1. Create a Statistics class to calculate central tendency, variability, percentile, and frequency distribution.
class Statistics:
    def __init__(self, data):
        self.data = sorted(data)

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        middle = self.count() // 2
        return self.data[middle] if self.count() % 2 else (self.data[middle - 1] + self.data[middle]) / 2

    def mode(self):
        value, count = Counter(self.data).most_common(1)[0]
        return value, count

    def var(self):
        return sum((value - self.mean()) ** 2 for value in self.data) / self.count()

    def std(self):
        return sqrt(self.var())

    def percentile(self, percent):
        index = round((percent / 100) * (self.count() - 1))
        return self.data[index]

    def freq_dist(self):
        counts = Counter(self.data)
        return sorted(((round(count / self.count() * 100, 1), value) for value, count in counts.items()), reverse=True)

    def describe(self):
        return {
            'Count': self.count(),
            'Sum': self.sum(),
            'Min': self.min(),
            'Max': self.max(),
            'Range': self.range(),
            'Mean': round(self.mean(), 2),
            'Median': self.median(),
            'Mode': self.mode(),
            'Variance': round(self.var(), 2),
            'Standard Deviation': round(self.std(), 2),
            'Frequency Distribution': self.freq_dist()
        }


# Calculate and print all Statistics values for the given ages sample.
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
for label, value in data.describe().items():
    print(f'{label}:', value)
print('50th Percentile:', data.percentile(50))

# === LEVEL 2 ===

# 1. Create a PersonAccount class with income, expense, totals, balance, and account information methods.
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append((amount, description))

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))

    def total_income(self):
        return sum(amount for amount, _ in self.incomes)

    def total_expense(self):
        return sum(amount for amount, _ in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f'{self.firstname} {self.lastname} | Income: {self.total_income():.2f} | Expense: {self.total_expense():.2f} | Balance: {self.account_balance():.2f}'

# Add income and expenses, then print the PersonAccount results.
account = PersonAccount('Beasty', 'Developer')
account.add_income(2500, 'Salary')
account.add_income(200, 'Freelance work')
account.add_expense(850, 'Rent')
account.add_expense(300, 'Food and transport')
print('Incomes:', account.incomes)
print('Expenses:', account.expenses)
print('Total income:', account.total_income())
print('Total expense:', account.total_expense())
print('Account balance:', account.account_balance())
print('Account info:', account.account_info())
