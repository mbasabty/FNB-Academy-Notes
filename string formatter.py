# username and message formatter

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio_msg = input("Enter a short bio message: ").strip()
replaced = bio_msg.replace("I am ", "I'm ")

username = first_name[0].lower() + "." + last_name.lower()
print("Your username is: " + username.title() + " and your bio message is: " + replaced + " length:" + str(len(replaced)))