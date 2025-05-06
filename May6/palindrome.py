def is_palindrome(s):
    # Convert the string to lowercase and remove spaces to make the check case insensitive and ignore the spaces
    s = s.lower().replace(" ", "")
    
    # Check if the string is equal to its reverse
    return s == s[::-1]  # [::-1] is the reversed copy of string s

# ask the user to input a word or string
word = input("Enter a word to check if it's a palindrome: ")

# Call the function and print the result based on return value
if is_palindrome(word):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")