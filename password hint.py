# Password hint tool

password = input("Enter your password: ").strip()
first_char = password[0]
last_char = password[-1]    
print(f"Password hint: {first_char}...{last_char}")

# Generate a hint by showing the first and last character of the password
