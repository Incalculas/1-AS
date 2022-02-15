# 1. summation of i^2 and i^3 with a loop and with formula
# for i^2
n = int(input("enter the value of n for calculating summation of i^2: "))
sum = 0
for i in range (0,n):
    sum += pow(i+1,2)
print("the summation of i^2 for given value of n calculated with a loop is:",sum)
print("the summation of i^2 for given value of n calculated with formula is:",int(n*(n+1)*(2*n+1)/6))

print("\n")

# for i^3
n = int(input("enter the value of n for calculating summation of i^3: "))
sum = 0
for i in range (0,n):
    sum += pow(i+1,3)
print("the summation of i^3 for given value of n calculated with a loop is:",sum)
print("the summation of i^2 for given value of n calculated with formula is:",int(n*n*(n+1)*(n+1)/4))

print("\n")

# 2. creating a list with a certain pattern
n = int(input("enter the length of the list with pattern: "))
x = []
for i in range(0,n):
    if(i%2):
        x.append(0)
    else:
        x.append(i+1)
print(x)

print("\n")

# 3. creating a list where nth element is the summation of i^2 upto n
n = int(input("enter the length of the list where nth element is sum of i^2 till n: "))
x = [1]
for i in range(1,n):
    x.append(x[i-1]+(i+1)**2) # we append the sum of the previous element and (index+1)^2 instead of calculating sum of i^2 until n from 1 for every index to save on resources
print(x)

print("\n")

# 4.calculation value of a math expression
n = int(input("enter the value of n for the math expression: "))
sum = 1
for i in range(0,n):
    sum = 1 + (i+1)/sum # we are able to do this because the math expression can be expressed as f(n) = 1 +n/f(n-1)
print("final value is:",sum)

print("\n")

# 5. Fibonacci series
x = [1,1]
n = int(input("enter the length of the list for Fibonacci series: "))-2
for i in range(0,n):
    x.append(x[-1]+x[-2]) # appending the sum of last 2 elements of the list, the definition of Fibonacci series
print(x)

print("\n")

# 6. calculating square root of a given number
c = 1
while (c): # the loop will run till c value changes to 0, which we will do once we get a valid input from the user. 
    n = int(input("enter the number to find the sqare root of: "))
    if(n<0):
        print("enter a valid input")
    else:
        print("the square root is:",n**(0.5))
        c = 0

print("\n")

# 7.1. tuple of student
student =(int(input("enter your age: ")),)
student = student + (input("enter your name: "),)
print("the tuple of the student is:",student)

print("\n")

# 7.2. list of tuple of students
students = []
for i in range(0,10):
    print("taking details of student",i+1)
    student = (int(input("age: ")),)
    student = student + (input("name: "),) # we have to add tuples to add a new element, because append doesn't work on tuples
    students.append(student)
print(students)

print("\n")

# 7.3. searching within this list of students
name = input("enter the name to be searched: ")
print("age/s of student/s of this name is:",end = " ")   
for i in range(0,10):
    if(name==students[i][1]):
        print(students[i][0],end="; ")

print("\n")

# 8. check missing digits in a mobile number
x = input("enter the phone number: ")
x = set([int(i) for i in x])  # string is converted to list, then each element is converted to int and finally it is made into a set all in 1 line.
y = set(range(0,10)) # creates a set of {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print("the missing digits are:",y-x) # by finding the difference between the 2 sets y and x, we get the missing digits

# can be compressed to 1 line like
# print("the missing digits are: ",set(range(0,10)) - set([int(i) for i in input("enter your phone number: ")]))

print("\n")

# 9. using list comprehension to separate a list 
n = int(input("enter number of students: "))
x = []
print("enter student roll numbers")
for i in range(0,n):
    x.append(input())

x = ["00" + i for i in x]
x = ["20MS"+i[-3] + i[-2] + i[-1] for i in x] # by adding "00" at the front and THEN considering only the last 3 characters, we generalise all roll numbers to the format we need

a = [i for i in x if int(i[4]+i[5]+i[6]) < 150 ]
print("list of group A students (roll number less than 150):",a)
b = [i for i in x if int(i[4]+i[5]+i[6]) > 150 ]
print("list of group B students (roll number more than 150):",b)

print("\n")

# 10. list comprehension for farenheit to celsius 
n = int(input("enter number of temperature values: "))
f = []
print("enter the values in Farenheit: ")
for i in range(0,n):
    f.append(float(input()))
c=[(i-32)*5/9 for i in f]
print("The same temperature in Celsius is:",c)

print("\n")

# 11. updating values from a tuple
print("enter the 5 scores")
x = ()
for i in range(0,5):
    x = x + (int(input()),)
print("current list of scores:",x)
for i in range(0,5):
    if(x[i]<50):
        x = list(x)
        x[i] += 5
        x = tuple(x)
print("updated list of scores:",x)