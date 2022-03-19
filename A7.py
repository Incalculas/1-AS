# 1.calculator

def ad(): # functions to do the operations
    print("Result: ",int(input("Give your first input: "))+int(input("Give your second input: ")))

def sub():
    print("Result: ",int(input("Give your first input: "))-int(input("Give your second input: ")))

def mult():
    print("Result: ",int(input("Give your first input: "))*int(input("Give your second input: ")))

def div(): # we don't do the print in 1 line in case second input is 0
    a = int(input("Give your first input: "))
    b = int(input("Give your second input: "))
    if b: print("Result:",a/b)
    else: print("math error")

c = 1
test = {1:ad,2:sub,3:mult,4:div} # for switch case
def f(x):
    return test.get(x)()
while c:
    x = int(input("\n=============calculator=============\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\nTo exit enter any other number\n"))
    if x not in [1,2,3,4]: # no default case in switch case, so we are checking for this before we call f()
        print("exiting......")
        break
    f(x) # calling the function to do the operation based on the input

# switch case was used here instead of the more natural choice of if, elif and else for no reason in particular

print()

# 2. finding euclidian distance between points

x = [ int(i) for i in input("enter point 1: ").split(' ') ] # taking input and converting points into a list, example '2 3' converts to [2,3]
y = [ int(i) for i in input("enter point 2: ").split(' ') ]
print("the distance between the points are: ",((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5) # output is a simple math expression

# To make things interesting we can consider the points to be in n dimensions instead of limitting to 2
# Below is a solution where the code assumes the dimension to be the point with less dimension
""" 
if (len(x) > len(y)):
    x,y = y,x
z = []
for i in range(0,len(x)):
    z.append(x[i] - y[i])
print("the dimension taken was,",len(z)," and the distance between the points is:",sum([ i**2 for i in z])**0.5)

"""

print()

# 3. finding points based on number of wins, losses and draws

x = [ int(i) for i in input("enter the number of wins, loss and draws with space separation: ").split(' ') ] 
# input is converted similar to how it was done in previous question
points = x[0]*2 + x[-1] # calculation of points
print("The points of the team is: ",points) # output
print("The highest possible points attainable for these many matches were:",sum(x)*2) # extra useful information
print("The points if the team had a equal chance of victory and defeat is: ",sum(x))

print()

# 4. Converting DNA sequence into RNA sequence

while True:
    dna = input("Enter the DNA sequence(case insesitive):\n").upper()
    if ( set(dna) - {'A','C','T','G'} != set() ):
        print("enter a proper DNA sequence")
    else:
        rna = []
        for i in dna:
            if i == 'T': rna.append('U')
            else: rna.append(i)
        print("The RNA sequence is:")
        print(''.join(rna))
        break

print()

# 5.

while True:
    dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    print("the DNA which was taken as input is:",dna,'\n')
    # dna = input("Enter the DNA sequence(case insesitive):\n").upper()
    # the above line should be used for user input
    if ( set(dna) - {'A','C','T','G'} != set() ):
        print("enter a proper DNA sequence\n")
    else:
        c = [0,0,0,0]
        for i in dna:
            if i == 'A':
                c[0] += 1
            elif i == 'C':
                c[1] += 1
            elif i == 'G':
                c[2] += 1
            else:
                c[3] += 1
        print("Adenine:",c[0],"\nCytosine:",c[1],"\nGaunine:",c[2],"\nThymine:",c[3])
        break

# different ways of counting are given below

"""
l = len(dna)
dna = dna.replace('A','') 
print("Adenine: ",l - len(dna))
l = len(dna)
dna = dna.replace('C','')
print("Cytosine: ",l - len(dna))
l = len(dna)
dna = dna.replace('G','')
print("Guanine: ",l - len(dna))
print("Thymine: ",len(dna))

print(dna.count('A'))
print(dna.count('C'))
print(dna.count('T'))
print(dna.count('G'))

"""
print()

# 6. modifying the input string

x = input("write the string to be arranged in alphanumerical order:\n").split(' ') # we make the input string into a list of words
x = set(x) # removes duplicates
x = ' '.join(sorted(x)) # joins the words into a string after sorting it alphanumerically with the help of sorted()
print(x)
# since this program is a set of simple functions, we can compress it into a single line
# print(' '.join(sorted((set(input("write the string that needs to be modified:\n").split(' ')))))

print()

# 7. checking a list and dictionary if it contains the given input

lst = ['I','think','therefore','I', 'am','said','Rene','Descartes']
dct = {'Rene' : 0, 'Descartes' : 1, 'I' : 2, 'think': 3}
# lst = input("enter the string: ").split(' ')
# print("enter input for dictionary with space interval
# dct = dict(zip( input("enter keys for dictionary").split(' ') , [ int(i) for i in input("enter values of dictionary").split(' ') ] ) 
# above 3 lines for manual input

k = input("enter the key, which is to be checked: ") 
a = ' not '
b = a
if ( k in lst ): a = ' ' # condition to check if k is in the list
if ( k in dct.keys() ): b = ' ' # condition to check if k is in the dictionary
kk = ''
if ( a == ' ' and b == ' ' ): kk = "\nThe value for the key is: " + str(dct.get(k)) # getting value from dictionary

print("The given key was",a,"found in the list\nThe given key was",b,"found in the keys of the dictionary",kk,sep='') # output

print()

#The program can be done with the method below as well

"""

if (k in lst):
    if( k in dct.keys() ):
        print("key is in both list and dictionary")
        print("value for the key is:",dct.get(k))
    else:
        print("the key was in the list but not in the dictionary")
else:
    if( k in dct.keys() ):
        print("the key was in dictionary but not in the list")
    else:
        print("the key is not in the list nor in the dictionary")

"""
