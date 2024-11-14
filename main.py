class Student:
    first_name = "Edwin"
    last_name = "Kasisi"
    gender = "Male"
    age = 26

class Person:
    def __init__(self, name, gender, marital_status, occupation):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.occupation = occupation

    def salutation(self):
        print(f"Good Morning {self.name}, you are {self.gender}, and {self.marital_status}")

    def display_name(self):
        print(f"I am {self.name}")

class Vehicle:
    def __init__(self, color, model, purpose):
        self.color = color
        self.model = model
        self.purpose = purpose

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)
    def area(self):
        return self.length *self.width
    def display(self):
        print(f"Length: {self.length}, Width: {self.width}")

class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def display1(self):
        return f"I am {self.name} and I am {self.age} years old"

class Manager(Employee):
    def __init__(self, name, age, salary, gender, education_level):
# super() what is going to be inherited from the parent class
        super().__init__(name, age, salary, gender)
        self.education_level = education_level

class Developer(Employee):
    def __init__(self, name, age, salary, gender, language):
        super().__init__(name, age, salary, gender)
        self.language = language

class SalaryEmployee(Employee):
    def __init__(self, name, age, salary, gender, weekly_salary):
        super().__init__(name, age, salary, gender)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary + self.salary


class HoursEmployee(Employee):
    def __init__(self, name, age, salary, gender, hours_worked, hourly_rate):
        super(). __init__(name, age, salary, gender)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return (self.hours_worked * self.hourly_rate) + self.salary

class CommissionEmployee(SalaryEmployee):
    def __init__(self, name, age, salary, gender, weekly_salary, commission):
        super().__init__(name, age, salary, gender, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission



class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def bankfees(self):
        fee = self.balance * 0.05
        return self.balance - fee

    def display2(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

class Deposit(BankAccount):
    def __init__(self, name, account_number, balance, deposit):
        super().__init__(name, account_number, balance)
        self.deposit = deposit

    def inputdeposit(self):
        amount = self.balance + self.deposit
        return amount


class Withdrawal(BankAccount):
    def __init__(self, name, account_number, balance, withdrawal):
        super().__init__(name, account_number, balance)
        self.withdrawal = withdrawal

    def inputwithdrawal(self):
         return self.balance - self.withdrawal


# todo_lists
class tasks = []

    def show_tasks():
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {'[Done] ' if task['done'] else ''}{task['task']}")

    def add_task(task_description):
        tasks.append({"task": task_description, "done": False})

    def mark_task_done(task_number):
        if 0 <= task_number:
            tasks[task_number]["done"] = True
        else:
            print("Invalid task number")



