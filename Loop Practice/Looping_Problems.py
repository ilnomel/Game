# 1. Printing 10 asterisks(*) like the following:
# * * * * * * * * * *

print("printing 10 asterisks in a line")
for i in range(10):
    print("*", end=" ")
    
# 3. Use two for loops to print 10x10 asterisks block

print("\n\nprinting 10x10 block of asterisks")
for row in range(10):
    for column in range(10):
        print("*", end=" ")
    print()
   
print("\nprinting 5x10 block")
for row in range(10):
    for column in range(5):
        print("*", end=" ")
    print()
    
print("\nprinting 20x5 block")
for row in range(5):
    for column in range(20):
        print("*", end=" ")
    print()
    
print("\n\n6.")
for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print()
    
print("\n\n7.")
for i in range(10):
    for j in range(10):
        print(i, end=" ")
    print()

print("\n\n8.")
for row in range(10):
    for column in range(row+1):
        print(column, end=" ")
    print()
    
print("\n\n9.")
for row in range(10):
    for column in range(10 - row):
        print(column, end=" ")
    print()
    
print("\n\n9.")
for row in range(10):
    for column in range(row):
        print(" ", end=" ")
    
    for column in range(10 - row):
        print(column, end=" ")
    print()
    
print("\n\n10.")
for i in range(10):
    for j in range(10):
        print(i*j, end=" ")
    print()
    
print("\n\n10.")
for i in range(1,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print()
    
print("\n\n10.")
for i in range(1,10):
    for j in range(1,10):
        if i*j < 10:
            print(" ", end=" ")
        print(i*j, end=" ")
    print()
    
print("\n\n11.")
for i in range(1,10): #range: 1-9
    for j in range(i): #range: 0-8
        print(j+1, end=" ")
    print()
    
print("\n\n11.")
for i in range(10):
    #count up
    for j in range(1, i+1):
        print(j, end=" ")
    #count down
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()
    
print("\n\n11.")
for i in range(10):
    #spaces
    for j in range(10-i):
        print(" ", end=" ")
    #count up
    for j in range(1, i+1):
        print(j, end=" ")
    #count down
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()

print("\n\n12.")
for i in range(10):
    #spaces
    for j in range(10-i):
        print(" ", end=" ")
    #count up
    for j in range(1, i+1):
        print(j, end=" ")
    #count down
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()
for i in range(10):
    for j in range(i+2):
        print(" ", end=" ")
    
    for j in range(1, 9-i):
        print(j, end=" ")
    print()
    
print("\n\n13.")
for i in range(10):
    #spaces
    for j in range(10-i):
        print(" ", end=" ")
    #count up
    for j in range(1, i+1):
        print(j, end=" ")
    #count down
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()
for i in range(10):
    for j in range(i+2):
        print(" ", end=" ")
    #count up
    for j in range(1, 9-i):
        print(j, end=" ")
    #count down
    for j in range(7-i, 0, -1):
        print(j, end=" ")
    print()