digit1 = input("Enter digit 1: ")
digit2 = input("Enter digit 2: ")
digit3 = input("Enter digit 3: ")

digits = [digit1, digit2, digit3]

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and i != k:
                print(digits[i] + digits[j] + digits[k])
