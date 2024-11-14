from main import Student, Employee, Manager, Developer, SalaryEmployee, HoursEmployee, CommissionEmployee, BankAccount, \
    Deposit, Withdrawal, add_task, show_tasks, mark_task_done
from main import Person
from main import Vehicle
from main import Rectangle

student1 = Student()
print(student1.first_name)
print(student1.last_name)
print(student1.gender)
print(student1.age)

student2 = Student()
print(student2.first_name)
print(student2.last_name)
print(student2.gender)
print(student2.age)

person1 = Person("Jones", "Female","Single", "Plumber")
person2 = Person("Ann", "Female","Married", "Teacher")
person3 = Person("Paul", "Male","Complicated", "Pilot")
print(person1.gender)
print(person3.marital_status)
print(person2.name)
print(f"Name: {person1.name}, Gender:{person1.gender}, Marital Status: {person1.marital_status}, Occupation: {person1.occupation}")

# create a vehicle class and implement three instances from it
vehicle1 =  Vehicle("White", "Mazda", "Personal")
vehicle2 =  Vehicle("blue", "Nissan", "PSV")
vehicle3 =  Vehicle("Grey", "Lorry", "Delivery")

print(vehicle1.model)
print(vehicle2.color)
print(vehicle3.purpose)
print(f"Color: {vehicle1.color}, Model:{vehicle1.model}, Purpose:{vehicle1.purpose}")

person1.salutation()
person2.salutation()
person3.salutation()

person1.display_name()
person2.display_name()
person3.display_name()

# write a rectangle class allowing a method perimeter that calculates the perimeter of a rectangle
# and method area of a rectangle, another method display that displays the length and width of an instance

rectangle1 = Rectangle(20, 15)
rectangle2 = Rectangle(35, 26)

print("perimeter:", rectangle2.perimeter())
print("area:", rectangle1.area())

rectangle1.display()
rectangle2.display()

employee1 = Employee("Judy", 33, 350000, "Female")
employee2 = Employee("Wayne", 24, 462000, "Male")
manager1 = Manager("Kelvin", 55, 769000, "Male", "Doctorate")
manager2 = Manager("Purity",35, 659000, "Female", "Master")
developer1 = Developer("Wesley", 23, 400000, "Male","Python")
developer2 = Developer("Cyndia", 20, 350000, "Female","Kotlin")
salaryemployee1 = SalaryEmployee("John",27, 100000, "Male", 25000)
salaryemployee2 = SalaryEmployee("Everline",40, 200000, "Female", 50000)
hoursemployee1 = HoursEmployee("Wafula", 39, 240000, "Male", 8, 1500)
hoursemployee2 = HoursEmployee("Faith", 24, 360000, "Female", 9, 2000)
commissionemployee1 = CommissionEmployee("James", 33, 455000, "Male", 100000,9000)
print(developer1.display1())
print(manager1.display1())
print(employee2.display1())
print(salaryemployee1.display1())
print(hoursemployee2.display1())

print(salaryemployee2.calculate_payroll())
print(hoursemployee1.calculate_payroll())
print(commissionemployee1.calculate_payroll())

# create a parent class bankaccount which represents a bank account with its respective attributes.
# create a deposit method that manages the deposit actions.
# create a withdrawal method which manages withdrawal actions.
# create a bankfees method that applies bankfees percentage of 5% on the balance in account.
# create display method to display account details.
# NB ensure the class has atleast 2 child classes

bankaccount1 = BankAccount("Joan", "D10001",20000)
bankaccount2 = BankAccount("Erik", "B10002", 36678)
deposit1 = Deposit("Winny", "F10003",44300,5400)
deposit2 = Deposit("Johnte","R10004",142000,21900)
withdrawal1 = Withdrawal("Njeri","J10005",399000,142000)
withdrawal2 = Withdrawal("Sam", "L10006",567899, 15990)

print(bankaccount1.bankfees())
print(bankaccount2.display2())
print(deposit1.inputdeposit())
print(deposit2.inputdeposit())
print(withdrawal1.inputwithdrawal())
print(withdrawal2.inputwithdrawal())



add_task("Data Analysis")
add_task("Data Presentation")
show_tasks()
mark_task_done(0)
show_tasks()



