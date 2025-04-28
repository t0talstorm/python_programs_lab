rows = int(input("Enter the number of rows(pattern 1 left aligned upside down): "))

for i in range(rows+1):
    for j in range(i):
        print("*", end="")
    
    print()
    

rows = int(input("Enter the number of rows(pattern 1 left aligned upside down): "))

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    
    print()
    
rows = int(input("Enter the number of rows (pattern 1 right aligned): "))

for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end="")
    
    for k in range(i):
        print("*", end="")
    
    print()
    

rows = int(input("Enter the number of rows (pattern 2 centre aligned): "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        if k % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")

    print()  

rows = int(input("Enter the number of rows (for the odd no. of stars): "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()
    
alphabets = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

char = input("Enter a character: ")

n = alphabets.index(char.upper()) + 1

for i in range(n):
    for j in range(n - i):
        if(alphabets[j] == char.upper()):
            print("",end="")
        else:
            print(alphabets[j], end="")

    if i > 0:
        for j in range(2 * i - 1):
            print(" ", end="")

    for j in range(n - i - 1, -1, -1):
        print(alphabets[j], end="")

    print("")
    
print()


# WHAT ACTUALLY NEEDS TO BE GOT ON JOURNAL 
rows = int(input("Enter the number of rows (upside down - triangle): "))

for i in range(rows,0,-1):
    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()
