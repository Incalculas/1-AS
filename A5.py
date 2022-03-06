import math
# 1. printing the prime numbers between 2 integers
first_int = int(input("enter a random integer: ")) # taking input of the 2 integers
second_int = int(input("enter a random integer: "))
def pon(a): # declaring a function to find if a number is prime
    condition = 1 # returning 1 can be used as true in if() statements
    i = 2 
    while(i<a/2): # seeing if any int from 2 till a/x divides a to see if a is prime or not
        if(a%i == 0):
            x = 0
            break # breaking once we get a factor of a which isn't a or 1 to avoid unnecessary calculations
        i += 1
    return(condition)  
if(first_int>second_int): # simple swap without a 3rd variable
    first_int = first_int + second_int
    second_int = first_int - second_int
    first_int = first_int - second_int
i = first_int + 1 # starting i from first_int + 1 since it's between x and second_int and not from x to second_int
l = []
while(i<second_int): # simple while loop runs from first_int + 1 till second_int - 1 and stores the number if it's prime
    if(pon(i)): 
        l.append(i)
    i += 1
print("prime numbers between",first_int,"and",second_int,"is",l) # output 

print()

# 2. finding e^pi via approximation
sum = 1 # the first term is added to the final outside the loop
term = 1 # the first term starts at 1
count = 1 # the count of the number of terms
while(term*math.pi/count > 0.0001): # we stop once the next term is less than 0.0001, so the final value is less than 0.0001 away from the final value
    term = math.pi*term/count # calculation of the next term
    sum = sum + term # adding the new term to the sum
    count += 1 # increasing count for each time the loop runs
print("value of e^pie via approximation is: ",sum) # all the expected outputs
print("the absolute value of e^pie ",math.e**math.pi)
print("difference is: ",abs( sum - math.e ** math.pi))
print("it took",count,"number of terms to get this value") 

print()

# 3. finding sin(pi/2) with approximations
s = math.pi/2 # first term of the expansion is pi/2, s is the variable name used for each term
su = s # su is short for sum and we are adding the first term outside the loop
i = 1 # we  use i to count
while(True):
    s = s*((math.pi/2)**2)/(4*i**2 + 2*i)*(-1) # finding the value of next term from the current term
    if(abs(s) < 0.0001): break # we break when the term is less than 0.0001 because the final sum would have already been closer than 0.0001 to pi
    su = su + s
    i += 1
print("finding value of sin(pi)") # output
print("the approximated value:",su)
print("absolute value:",math.sin(math.pi/2))
print("absolute difference:",abs(su-math.sin(math.pi/2)))
print("number of terms used is:",i)

print()

# 4. printing a pattern
l = 10 # height of pattern is 10
y = " " 
x = "A"
i = l 
print("the pattern:")
while(i>-1): # simple while loop to print the pattern
    for j in range(0,i):
        print(y,end="")
    for j in range(0,l-i):
        print(x,end="")
    for j in range(0,l-i):
        print(x,end="")
    print()
    i -= 1

print()

# 5. checking if 3 sticks can form a triangle based on their lenghts
x = (int(input("enter the length of first stick: ")), int(input("enter the length of second stick: ")), int(input("enter the length of third stick: ")))
# a tuple of the 3 sides of triangle, input from the user
def t(a,b,c): # function which checks if the sides can form a triangle
    x = 0
    if((a+b > c) and (a+c > b) and ((b+c) > a)):
        x = 1
    return(x)
if(t(x[0],x[1],x[2])): # calling the function
    print("the sticks can form a triangle")
else:
    print("the sticks can't form a triangle")

print()

# 6. finding value of pi accurate to the 3rd decimal digit with expansion of arctan
def f(x,n): # function to find the sum of the expansion to a particular number of terms
    term = x  # first term is just x
    su = term  # su is sum, to avoid using variable name same as inbuilt function sum()
    i = 1
    while(i<n):
        term = (term*x*x)*(2*i-1)*(-1**i)/(2*i+1)  
        su += term
        i += 1
    return(su) 
i = 1
# to avoid using pi in the while loop condition, we check the last term calculated to be small enough 
# using pi in the while loop condition would mean we used pi to approximate pi which doesn't make sense
while(abs(f(1/(3**0.5),i+1) - f(1/(3**0.5),i))*6 > 0.001): 
    i += 1
print("apprixmated value of pi accurate to the 3rd decimal digit:",6*f(1/(3**0.5),i)) # output
print("real value of pi:",math.pi)
print("the absolute difference is:",abs(6*f(1/(3**0.5),i)-math.pi))
print("value of n in f(x,n) ie: number of terms:",i)

"""
# alternate code which doesn't use function f to find approximation of pi, this is faster to execute since we only calculate every term once
s = 1/3**0.5
su = s 
i = 1
while(True):
    print(6*s)
    s = (s/3)*(2*i-1)*(-1**i)/(2*i+1)  
    if (6*abs(s) < 0.001): break
    su += s
    i += 1
print()
print(6*su)
print(math.pi)
print(abs(math.pi-6*su))
"""

print()

# 7. finding number of iterations of a function, needed to get x = 10 to be less than 2 
def f(x): return(x**0.9) # this is a simple function which returns the input powered to 0.9
x = 10
i = 1 # to keep track of how many times the loop runs
print("value of x changes as:")
while(x):
    print(x)
    x = f(x)
    if (x<2): 
        x = f(x)
        print(x)
        break
    i += 1
print("\nthe function was executed on x",i,"number of times to reach less than 2 from 10")  
