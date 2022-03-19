import math
# 1. printing every term of a series
def g(n):
    sumg = 0 # sumg will be the sum of series g() 
    for i in range(1,n+1): # a simple for loop from 1 to n
        sumg += i/(i+1) # increasing sum by each term
    return sumg # returning the final sum
for i in range(0,20): # simple while loop to call the function from 1 to 20
    print(g(i+1))  

print()

# 2. calculating factorial
def fact(x):
    value = 1 # variable for final value of factorial
    for i in range(0,x): # simple for loop to calculate factorial 
        value *= i+1
    return value
for i in range(0,8): # simple for loop to print factorials of number 1 to 8
    print("factorial of",i+1,"is: ",fact(i+1))

print()

# 3. returning the value of sin(2t)
def sin2(x): return math.sin(2*x) # simple function to return sin(2t)
for i in range(0,10):
    print("value of sin(2t) when t is",i*10," is:",sin2(i*math.pi/18))

print()

# 4.deciphering the given input
text = list(input("enter a string to be deciphered: ")) # input converted to list for our ease
i = 0
for i in range(0,len(text)-1,2): # while loop to run at all odd elements of a list
    temp = text[i]  # swap
    text[i] = text[i+1] 
    text[i+1] = temp 
text = ''.join(text) # forming the string from the list
print(text)

print()

# 5. removing the brackets and characters within it from a given string input
x = input("enter the list to be processed: ") # input
x = x.split('(') # spliting at (
x = [ i.split(')') for i in x ] # spliting at )
x = [ i[-1] for i in x] # taking in characters only after ) and before (
x = ''.join(x) # final string
print(x) 

# print(''.join([i.split(')')[-1] for i in input("enter a string to be processed: ").split('(')]))
# the same can be compressed into a single line

print()

# 6. taking input and counting number of odd or even integers
n = int(input("enter number of input that will be given: ")) 
x = 0
for i in range(0,n): # simple for loop to take input into a list
    print("enter value ",i+1,": ",end='')
    x += int(input())%2
print("number of even integers is: ",n-x) # output
print("number of odd integers is: ",x) 

print()

# 7. sum of series
three = '3' # to make it easier to find each term of the series
n = int(input("enter the number of terms in the series: "))
su = 0 
for i in range(0,n):
    su += int(three*(i+1)) # each term of the series is added to the sum
print("sum of series is up to term ",n,"is: ",su) # output

print()

# 8. checking for strong numbers from 1 to 100,000
def strong(x):
    sum = 0
    for i in list(str(x)): # to separate each digit 
        sum += fact(int(i)) # previously declared function is called (declared in problem 2)
    if(sum == x):
        return True
    else: 
        return False
print("strong numbers from 1 till 100000 are: ")
for i in range(0,100000): #simple for loop to print all strong numbers
    if(strong(i+1)): print(i+1)

print()

# 9. finding the day of a date

m = [0,3,3,6,1,4,6,2,5,0,3,5] # this will help us determine the day of 1st of each month
print("enter a date between 1900-1-1 and 2100-12-31") # because we are not considering the fact that 2100,2200,2300 all are not leap years
ye = int(input("enter the year: ")) # input of the date
mo = int(input("enter the month in numbers: "))
d = int(input("enter the date: "))
da = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] # meant for the output
e = 0 # da[e%7] is the day of a date, we need to calculate e of every date
e += (ye-1900)%7 
e += ((ye-1901)-(ye-1901)%4)/4 # we calculated e for 1st jan of given year
e += m[mo-1] 
if(ye%4 == 0):
    if(mo>2): e += 1 # calculation of e for 1st of the given month
e += d%7 + 6 # e calculated for given date
e = e%7 
print(da[int(e)])
