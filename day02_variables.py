# Day 02 - Variables & Data Types 

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))
is_student = input("Are you a student? (yes/no): ")
current_year = int(input("Enter current year: "))

# Converting input to boolean
is_student = True if is_student.lower() == "yes" else False

# Calculations
birth_year = current_year - age
height_cm = height * 100

# Output
print("\n----- User Details -----")
print(f"Name        : {name}")
print(f"Age         : {age}")
print(f"Birth Year  : {birth_year}")
print(f"Height      : {height_cm} cm")
print(f"Student     : {is_student}")

# Data types check
print("\n----- Data Types -----")
print("Type of name       :", type(name))
print("Type of age        :", type(age))
print("Type of height     :", type(height))
print("Type of is_student :", type(is_student))
