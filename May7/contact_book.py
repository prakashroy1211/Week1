contacts = {} # initialize an empty dictionary

# Open and read from contacts.txt
file = open("contacts.txt", "r")
for line in file:
    name, phone = line.strip().split(":")
    contacts[name] = phone
file.close()

# Get new contact from user
name = input("Enter contact name: ")
phone = input("Enter phone number: ")

# Add to dictionary
contacts[name] = phone

# Save updated contacts to contacts.txt file
file = open("contacts.txt", "w")
for name, phone in contacts.items():
    file.write(f"{name}:{phone}\n")
file.close()

# Print all contacts
print("\nAll Contacts:")
for name, phone in contacts.items():
    print(f"{name} : {phone}")