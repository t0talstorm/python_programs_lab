
def multi(input_nos):
    result = 1
    for char in input_nos:
            result = int(char) * result  
    return result

input_nos = input("Enter any digit number : ")
number = multi(input_nos)
print(f"The multiplication of the digits is : {number}")
