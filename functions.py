def my_function():
    print("GoodMorning Wesley")
    print("GoodMorning Chelah")
    print("GoodMorning Kasisi")
my_function()

def my_string():
    hello = "Hello Everline, hope you're well"
    print(hello)
my_string()

def arg(name):
    print(name)

arg("Alex")
arg("Wayne")
arg("Charity")
arg("Tom")
arg("Samantha")
def my_func(first_name):
    print("Hello" + first_name + "Please enter")
    print(f"FirstName: {first_name}")
my_func("Wesley")

def my_func2(first_name, age):
    print(f"Hello {first_name} your age is {age} years old")

my_func2( "Felix", 39)
my_func2( "Wesley", 23)
my_func2( "Darius", 19)

def my_func3(first_name, lastname, age):
    print(f"Hello {first_name} {lastname} your age is {age} years old")
my_func3("Felix","Kegode",23,)
my_func3("Kamau","Joshua",54)
my_func3("John","Waweru",30)

# create a function that takes two numbers as arguments and performs
# a summation then displays the summation

def summation(number1, number2):
    Add = number1 +number2
    return Add
print(summation(50, 79))

def multiply(a,b):
    result = a*b
    return result
print(multiply(45, 76))

def age_calc(current_age):
    new_age = current_age + 8
    return new_age
print(age_calc(23))

def promote(name, age):
    if age >= 5 and age <= 7:
        return f"{name} you are {age} years old and you are promoted to grade 1"
    elif age == 8:
        return f"{name} you are {age} years old and you are promoted to grade 2"
    elif age > 8 and age <= 10:
        return f"{name} you are {age} years old and you are promoted to grade 3"
    else:
        return f"{name} you are not supposed to be in lower primary"
print(promote("Wesley",9))
print(promote("Lubia", 6))
print(promote("Amani", 13))

# create a function called greet that takes a persons name as an argument and returns
# a greeting message. if the name is 'Alice' or 'Bob' it returns a personalised greeting,
# for any other name it should return a general greeting
def greet(name):
    if name == "Bob":
        return f"Hello Bob, How are you?"
    elif name == "Alice":
        return f"Hello Alice, How are you?"
    else:
        return f"Hello, How are you?"
print(greet("Bob"))
print(greet("Austin"))
print(greet("Alice"))
print(greet("Brendah"))

# write a python that finds a maximum of three numbers
def maximum(a, b, c):
    maxi = max(a, b, c)
    return maxi
print(maximum(15, 23,67))
print(maximum(278, 300,124))
print(maximum(2800, 150,2799))


# create a python function that sums all numbers in a list
def sum_list(numbers):
    return sum(numbers)
numbers = [1, 2, 3, 4, 5, 6]
print(sum_list(numbers))





