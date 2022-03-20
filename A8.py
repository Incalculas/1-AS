#
#  CS1101: assignment 8 by Raakesh M
#  Roll number: 21MS116
#



# 1. converting given RNA sequence into list of codons

while True: # to run the program till we get a valid input
    rna = input("enter the RNA sequence: ").upper() # input
    #rna = "AUGGGAACUUCACUACGUAAAUAG" # for testing purposes
    if(set(rna) - {'A','C','G','U'} == set()): # checking if given sequence is valid
        codons = []
        for i in range(0,len(rna)-2,3): # a simple loop to get all the codons into groups of 3
            codons.append(rna[i]+rna[i+1]+rna[i+2])
        print(codons)
        freq = list(sorted(set(codons))) # removing duplicates
        l = len(codons)
        for i in freq: 
            j = codons.count(i)*100/l
            print(i,' : 1/',int(1/(codons.count(i)/l)),'\t%.2f' %j,'%',sep='') 
            # printing frequency to the closest in the form of 1/n and the the frequence in %
        break
    else: 
        print('\nThis is not a valid RNA sequence\n') 

print()

# 2. Translating mRNA sequence into Amino acids

while True: # to run the program till we get a valid input
    #mrna = "AUGGGAACUUCACUACGUAAAUAG" # for testing purposes
    mrna = input("enter the RNA sequence: ").upper() 
    amino = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',# UU
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',# UC
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '0', 'UAG': '0',# UA
        'UGU': 'C', 'UGC': 'C', 'UGA': '0', 'UGG': 'W',# UG
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',# CU
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',# CC
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',# CA
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',# CG
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',# AU
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',# AC
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',# AA
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',# AG
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',# GU
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',# GC
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',# GA
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',# GG
            }   # for translation

    if(set(mrna) - {'A','C','G','U'} == set()): # checking validity of the given sequence 
        codon_amino = []
        for i in range(0,len(mrna)-2,3): # grouping 3 nucleotides together
            codon_amino.append( mrna[i] + mrna[i+1] + mrna[i+2] )
        print('\n',codon_amino,'\n')
        i = 0
        translation = ''
        while(i < len(codon_amino)):
            translation += amino.get(codon_amino[i]) # translating the codons into associated amino acids
            i += 1
        print('full translation of all codons is:\n',translation,sep='') # prints entire translation including start and stop codon
        print('\n(the 0s represent stop codon)\n')
        if(translation.count('M') < 2 and translation.count('0') <2):
            print('The translation is:',translation.split('0')[0].split('M')[0])
        # this covers "normal" cases with only 1 stop and 1 start codon at max
        else:
            print('there are multiple instances of start/stop codon')
            print('the translation split at the points of start and stop codons will be:')
            for i in translation.split('M'):
                for j in i.split('0'):
                    print(j)
        # for weird cases of more than 1 start/stop codon, we just print by splitting at both stop and start codon
        break
    else: 
        print('\nThis is not a valid RNA sequence\n')


# 3. Formatting a float variable 

from math import pi

r = float(input('\nenter the radius: ')) # input
v = pi*r*r*r*4/3 # calculation of the volume
print('The volume of sphere with different formats are:\n%.1f\n%.2f\n%.3f\n%.4f'%(v, v, v, v)) 
# printing with the right formating

print()

# 4. try and except

try:
    x = float(input('enter a number: ')) # input
    print('the square root is %.3f'%(x**0.5)) # printing the square root
except:
    print('the given number is either not a number or is a number but below 0') # in case Try code block doesn't run without error

print('Done') 

# indicating the end of this problem, this assignment and all of this course's assignments

