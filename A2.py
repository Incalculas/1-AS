# 1. printing serial number and name 15 times
x = "Raakesh"
for i in range(0,15):
    print (i+1,x)

print("\n")

# 2. printing serial number and name 15 times for when integer is multiple of 3
x = "Raakesh"
for i in range(0,15):
    if ((i+1)%3 == 0):
        print (i+1,x)

print("\n")

# 3. loop of outputting string
x = "abcdefghijkl"
for i in range(0,len(x)):
    print(x[i:len(x):1])

print("\n")

# 4. finding the max in a list
a = [0, 3, 1, 2, 8, 9, 0, 4, 7]
b = [0, -1, -3, -4, 3, 8, 9, 11, -2]
m = a[0]
for i in range(0,len(a)):
    if(m<a[i]):
        m = a[i]
print("biggest number in the first list is",m)
m = b[0]
for i in range(0,len(b)):
    if(m<b[i]):
        m = b[i]
print("biggest number in the second list is",m)

print("\n")

# 5. comparing results of finding max manually and using max and min function
a = [0, 3, 1, 2, 8, 9, 0, 4, 7]
b = [0, -1, -3, -4, 3, 8, 9, 11, -2]
m = a[0]
for i in range(0,len(a)):
    if(m<a[i]):
        m = a[i]
print("biggest number in the first list found without max function is",m)
print("biggest number in the first list found with max function is",max(a))
print("\n")
m = b[0]
for i in range(0,len(b)):
    if(m<b[i]):
        m = b[i]
print("biggest number in the second list without max function is",m)
print("biggest number in the second list with max function is",max(b))
print("\n")

m = a[0]
for i in range(0,len(a)):
    if(m>a[i]):
        m = a[i]
print("smallest number in the first list found without min function is",m)
print("smallest number in the first list found with min function is",min(a))
print("\n")
m = b[0]
for i in range(0,len(b)):
    if(m>b[i]):
        m = b[i]
print("smallest number in the second list without min function is",m)
print("smallest number in the second list with min function is",min(b))
print("\n")

# 6. generating the mail ID 
email = []
email.append(input("enter your name here:"))
year = input("enter your year of joining here:")
y = year[len(year)-2] + year[len(year)-1]
email.append(y)
email.append(input("enter your course ID here:"))
email.append(input("enter your student ID here:"))
email.append("@iiserkol.ac.in")
finalmail = "".join(email)
print("your generated email ID is:",finalmail)

print("\n")

# 7. adding integers stored as strings
str1 = "123"
str2 = "234"
str3 = "456"
x = []
x.append(int(str1))
x.append(int(str2))
x.append(int(str3))
print("sum of the 3 numbers is:",sum(x),", product of the 3 numbers is:",x[0]*x[1]*x[2],"and the average of the 3 numbers is:",sum(x)/3)

print("\n")

# 8. take input of 5 numbers using loop and print the sum
x = []
print("enter your numbers here:")
for i in range (0,5):
    x.append(int(input()))
print("the sum of the numbers is:",sum(x))

print("\n")

# 9. take list of marks and sort it and manipulate it 
x = []
print("enter student marks here:")
for i in range (0,10):
    x.append(int(input()))
for i in range (0,len(x)):
    for j in range (0,len(x)-i-1):
        if(x[j]<x[j+1]):
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp 
print("sorted list of marks:",x)
for i in range(0,len(x)):
    if(x[i]<45):
        x[i]+=5
print("mark list after grace marks:",x)
c = 0
for i in range(0,len(x)):
    if(x[i]<50):
        c+=1
print("number of failing marks is:",c)

print("\n")

# 10. sorting a list, removing the max and min 
numbers = []
print("enter your numbers here:")
for i in range (0,10):
    numbers.append(int(input()))
for i in range (0,len(numbers)):
    for j in range (0,len(numbers)-i-1):
        if(numbers[j]<numbers[j+1]):
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp 
print("sorted list of numbers:",numbers)
del numbers[0]
del numbers[len(numbers)-1]
print("new list of numbers:", numbers)