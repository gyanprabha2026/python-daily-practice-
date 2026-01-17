# day03 - Conditional Statements


# 1. Check the entered number is EVEN or ODD

num = int(input("Enter a number : "))

if num % 2 == 0:
    print(f"{num} is an EVEN number")
else:
    print(f"{num} is an ODD number")
print()


# 2. Check the student is PASS or FAIL

stu_marks = int(input("Enter student marks : "))

if stu_marks >= 33:
    print(f"Student with marks {stu_marks} is PASS")
else:
    print(f"Student with marks {stu_marks} is FAIL")
print()


# 3. Check the Voting Eligibility

age = int(input("Enter your age : "))

if age >= 18:
    print("You are Eligible for Vote ")
else:
    print("You are Not Eligible for Vote")
print()


# 4. Grading System

marks = int(input("Enter your marks : "))

if marks >= 85:
    print("Grade A")
elif marks >= 65:
    print("Grade B")
elif marks >= 45:
    print("Grade C")
elif marks >=33:
    print("Grade D")
else:
    print("Fail")
