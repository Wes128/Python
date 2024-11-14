# lists
employees = ['Peter','John','Smith','Esther']
print(employees)
print(employees[1])
print(employees[1:4])
        # to change the name at an index
employees[3] = 'Wesley'
print(employees)
        # to add an item at the end
employees.append('Kasisi')
print(employees)
        # to insert a name at an index
employees.insert(0,'juliana')
print(employees)
        # to add more than one item
employees.extend(['Edwin','Cyndia','Susan'])
print(employees)

# tuples
languages = ('Python','Java','Kotlin')
print(languages)
print(languages[1])
print(languages[1:3])
# sets
students = {'Everline','Doreen','Lydiah','Mercy'}
print(students)
if 'Everline' in students:
    print('Everline')
if 'Doreen' in students:
    print('Doreen')
if 'Lydiah' in students:
    print('Lydiah')
if 'Mercy' in students:
    print('Mercy')
if 'Susan' in students:
    print('Susan')
else:
    print('not present')

students.add('Charles')
print(students)
students.update('Reuben')
print(students)
students.remove('Charles')
print(students)

# dictionary
pupil = {
    'fist_name' : 'Chris',
    'last_name' : 'Njeu',
    'email': 'njue@gmail.com',
    'gender':'Female',
    'birthyear':'2000'
}
print(pupil)
print(pupil['email'])
pupil['skintone'] = 'brown'
print(pupil)

if 'skintone' in pupil:
    print('Yes it is present')
else:
    print('Not present')

# create a random dictionary and illustrate how to check existence of a key
staffs = {
    'fist_name' : 'Wesley',
    'last_name' : 'Kasisi',
    'email': 'wes@gmail.com',
    'gender':'Male',
    'Employee_Id':'D2024W',
    'Department':'Planning'
}
print(staffs)
if 'company' in pupil:
    print('Yes it is present')
else:
    print('Not present')
# take 4 users age inputs perform logical operations with the values
age1 = int(input("Enter age1: "))
age2 = int(input("enter age2: "))
age3 = int(input("enter age3: "))
age4 = int(input("enter age4: "))
sum = age1+age2+age3+age4
diff = age2-age4

print(sum)
print(diff)