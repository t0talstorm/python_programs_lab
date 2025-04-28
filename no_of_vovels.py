#Write a function to find the number of vowels in the given string

def no_of_vovels(input_str):
    result = 0
    for char in input_str:
        if char in "aeiouAEIOU":
            result += 1  
    
    return result

string = input("Enter any string : ")
number = no_of_vovels(string)
print(f"The number of vovels in the given string is : {number}")
