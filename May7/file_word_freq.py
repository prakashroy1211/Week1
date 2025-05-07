# filename from the user
filename = input("Enter the filename: ") # enter the filename with .txt

# Open and read the file
file = open(filename, 'r') # r is read mode
text = file.read() # copying it to text variable
file.close()

# Convert text to lowercase and split into words
words = text.lower().split()

# Initialize an empty dictionary
word_count = {}

# Count the frequency of each word
for word in words:
    word = word.strip(".,?")  # Remove punctuation from ends
    if word == "":
        continue
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print each word and its frequency
print("Word Frequencies:")
for word in word_count:
    print(word, ":", word_count[word])