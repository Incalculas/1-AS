# 1. flattening a nested list structure
x = [0, 10, [20, 30], 40, 50, [60, 70,[10,10,[10]], 80], [90, 100,[10,20], 110, 120, [90, 100, 110, 120]]]
y = []
def flat(a):
    for i in a:
        if(type(i) == list):
            flat(i)
        else:
            y.append(i)
print("original list is:",x)
flat(x)
print("flattened list is:",y) 

print("\n")

# 2. taking elements of a matrix one at a time
r = int(input("Enter no. of Rows: "))
c = int(input("Enter no. of Columns: "))
x = []
for i in range(0,r):
    y = []
    for j in range(0,c):
        print("Enter element at Row:", i+1,"; Column: ", j+1,":",end=" ")
        y.append(int(input()))
    x.append(y)
print("\nThe matrix is:")
for i in range(0,len(x)):
    for j in range(0,len(x[i])):
        print(x[i][j],end=" ")
    print("")

print("\n")

# 3. removing recurring elements from a list
a = [3, 7, 13, 9, 7, 5, 13, 17, 23, 17, 7, 29]
b = ["A", "E", "E", "O", "A"]
c = []
d = []
for i in a:
    if i not in c:
        c.append(i)
for i in b:
    if i not in d:
        d.append(i)
print("the old lists are:\n",a,"\n",b)
print("the new lists are:\n",c,"\n",d)

"""
alternate shorter method if order of elements don't matter 
print("the old lists are:\n",a,"\n",b)
print("the new lists are:\n",list(set(a)),"\n",list(set(b)))
"""

print("\n")

# 4. taking a list of non 0 integers from user to
c = 1
x = []
print("enter numbers to find average of, to stop taking inputs, enter 0")
while (c):
    c = int(input("enter a number: "))
    x.append(c)
x.pop()
print("the list is:",x)
if len(x):
    print("average of the numbers is: ", sum(x)/len(x))
else:
    print("no average to calculate with no elements in the list")
print("\n")

# 5. making a list of particular pattern
numbers = list(range(1,101))
squares = []
print("the list numbers is:", numbers)
for i in range(0,len(numbers)):
    squares.append(numbers[i])
    squares.append(numbers[i]**2)
print("the list squares is:", squares)

print("\n")

# 6. updating a dictionary and removing the first key
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("dictionary before updating: ",squares)
for i in range (6,10):
       squares.update({i:i**2})
print("updated dictionary is: ",squares)
x = list(squares.items())
squares.pop(x[0][0])
print("the key from the dictionary which is going to be deleted is:",x[0])
print("the dictionary after deleting the first element is: ",squares)

print("\n")

# 7. removing last element from each list in a nested list
arra = [[1, 2, 3, 4],[4, 5, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15]]
print("current nested list: ",arra)
for i in range(0, len(arra)):
    arra[i].pop()
print("the same nested list after modifications: ",arra)

print("\n")

# 8. sum of all values of a dictionary
x = {'a': 100, 'b':200, 'c':300}
print("first dictionary is: ", x)
print("sum of values of first dictionary is: ", sum(x.values()))
y = {'x': 25, 'y':18, 'z':45}
print("second dictionary is: ", y)
print("sum of values of second dictionary is: ", sum(y.values()))

# this can be done with just 1 line of code and without declaring any variable too as shown below in a comment
# print("first dictionary is: ",{'a': 100, 'b':200, 'c':300},"\nsum of values of first dictionary is: ", sum({'a': 100, 'b':200, 'c':300}.values()),"\nsecond dictionary is: ", {'x': 25, 'y':18, 'z':45},"\nsum of values of second dictionary is: ", sum({'x': 25, 'y':18, 'z':45}.values()))

print("\n")

# 9. Getting certain output from fixed tuple
t_o_t = (('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul'), ('sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'))
print(t_o_t[0][3],",",t_o_t[1][5])
print(t_o_t[0][0],",",t_o_t[1])

print("\n")

# 10. converting a list to dictionary
x = [2, 3, 5, 6, 7, 8]
y = {}
i = 0
print("original list is:", x)
while(i<len(x)):
    y.update({x[i]:x[i+1]})
    i += 2
print("dictionary derived from the list is:",y)
