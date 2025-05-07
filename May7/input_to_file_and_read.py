# Ask the user to enter some text
user_input = input("Enter some text to save to a file: ")

# Save the input to a file
file = open("user.txt", "w")  # 'w' = write mode (creates file if not exist)
file.write(user_input)
file.close()

# Read the content back from the file
file = open("user.txt", "r")  # r is read mode
content = file.read()
file.close()

# Display the content
print("\nContent from the file:")
print(content)