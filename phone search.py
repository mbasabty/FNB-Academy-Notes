# Phone Directory Search

# Dictionary of contacts
contacts = {
    "Sipho": "0821112222",
    "Lebo": "0833334444",
    "Aisha": "0765556666"
}

# Ask the user for a name
name = input("Enter the friend's name to search: ")

# Check if the name exists as a key
if name in contacts:
    print(f"Found! {name}'s number is {contacts[name]}")
else:
    print("Contact not found.")