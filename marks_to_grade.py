marks1 = float(input("Enter marks for subject 1 (out of 100): "))
marks2 = float(input("Enter marks for subject 2 (out of 100): "))
marks3 = float(input("Enter marks for subject 3 (out of 100): "))
marks4 = float(input("Enter marks for subject 4 (out of 100): "))
marks5 = float(input("Enter marks for subject 5 (out of 100): "))

total_percent = ((marks1 + marks2 + marks3 + marks4 + marks5)/500)*100

if total_percent >= 90:
    grade = "A"
elif total_percent >= 80:
    grade = "B"
elif total_percent >= 70:
    grade = "C"
elif total_percent >= 60:
    grade = "D"
elif total_percent >= 50:
    grade = "E"
else:
    grade = "F"

print(f"Total Marks: {total_percent}")
print(f"Grade: {grade}")
