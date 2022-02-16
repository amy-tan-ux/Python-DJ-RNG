import random
from random import randint

# Exact Bounded Knapsack
# Space Complexity - O(nb)
# Time Complexity - O(nb^2)

# Object of knapsack is to maximize value while keeping
# within weight constraints and max constraints.
# n is the number of items
# c is the vector containing the values of each item
# a is the vector containing the weights of each item
# m is the vector containing the maximum quantity of each item
# b is the capacity of the knapsack

def knapsack(n,c,a,m,b):
    
    # Initializing Data Tables to Store Intermediate Values
    hash_of_values={}
    table_of_objects=[[0 for x in range(n)] for y in range(b+1)]

    # Initializes the first row of "hash_of_values"
    for x in range(n):
        hash_of_values[(x,0)]=0
    # Initializes the first column of "hash_of_values"
    for y in range(b+1):
        t=min(y//a[0],m[0])
        hash_of_values[(0,y)]=t*c[0]
        table_of_objects[y][0]=t

    # Iterates through the the data tables and updates the values of the entries of "hash_of_values" 
    # and "table_of_objects". 
    for x in range(1,n):
        for y in range(1,b+1):
            t=min(y//a[x],m[x])
            
            if t == 0:
                hash_of_values[(x,y)]=hash_of_values[(x-1,y)]
            else:
                aux=[(hash_of_values[(x-1,y - j*a[x])] + j*c[x]) for j in range(t+1)]
                s=aux.index(max(aux))
                hash_of_values[(x,y)]=(hash_of_values[(x-1,y - s*a[x])] +s*c[x])
                table_of_objects[y][x]=s

    # Initializes the solution vector "taken_objects"
    taken_objects=[0]*n
    # Iterates through the entries of "table_of_objects" to update "taken_objects"
    x=n-1
    y=b
    
    while x>=0:
        taken_objects[x]=table_of_objects[y][x]
        y=y-(taken_objects[x]*a[x])
        x=x-1

    return(taken_objects)


# Order of notes
# semibrieve, dotted minim, minim, dotted crotchet, crotchet, dotted quaver, quaver, dotted semiquaver, semiquaver, dotted demisemiquaver, demisemiquaver

# n is the number of types of notes (see above)
n=11

# c is the value vector
c=[randint(1,250), randint(1,175), randint(1,150), randint(1,125), randint(1,100), randint(1,50), randint(1,35), randint(1,20), randint(1,15), randint(1,10), randint(1,5)]

# a is the weight vector (given by proportion of whole note multiplied by 64)
a=[64, 48, 32, 24, 16, 12, 8, 6, 4, 3, 2]

# m is the max vector
m=[randint(0,1), randint(0,1), randint(0,2), randint(0,2), randint(0,4), randint(0,5), randint(0,8), randint(0,10), randint(0,16), randint(0,21), randint(0,32)]

# b is the number of beats per measure (given by time signature)
b=64

ans=knapsack(n,c,a,m,b)
print(ans)

