def remove_punctuations(input_str):
    result = ""
    for char in input_str:
        if char not in ",.:!?":
            result += char  
    
    return result

old_string = input("Enter any string : ")
new_string = remove_punctuations(old_string)

print(new_string)
