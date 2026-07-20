# Practical Task 
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
favorite_number = input("Enter your favorite number: ")

print(f"Welcome, {first_name.upper()}!")
age_in_months = int(age) * 12
rounded_favorite_number = round(float(favorite_number))
print(type(first_name))
print(type(surname))
print(type(age))
print(type(favorite_number))