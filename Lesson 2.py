# creating a professional email generator using Python

first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

username = first_name.lower() + "." + last_name.lower()
print("Your professional email address is: " + username + "@company.com")