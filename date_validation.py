
Date, Month, Year = map(int, input("Enter date in format of DD/MM/YYYY: ").split("/"))

if Year > 0:
    if 1 <= Month <= 12:
        if Month in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= Date <= 31:
                print("Valid Date")
            else:
                print("Invalid Date: Month has only 31 days")
        elif Month in [4, 6, 9, 11]:
            if 1 <= Date <= 30:
                print("Valid Date")
            else:
                print("Invalid Date: Month has only 30 days")
        elif Month == 2:
            if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
                if 1 <= Date <= 29:
                    print("Valid Date")
                else:
                    print("Invalid Date: February has only 29 days in a leap year")
            else:
                if 1 <= Date <= 28:
                    print("Valid Date")
                else:
                    print("Invalid Date: February has only 28 days")
    else:
        print("Invalid Month: Month should be between 1 and 12")
else:
    print("Invalid Year: Year should be a positive number")
