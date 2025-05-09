students = {} # Initializa an empty dictionary

# add student function
def add_student(student_id, name):
    students[student_id] = name
    print(f"Added student: {name}")

# remove student function
def remove_student(student_id):
    if student_id in students:
        print(f"Removed student: {students[student_id]}")
        del students[student_id]
    else:
        print("Student not found")

# student search function
def search_student(student_id):
    if student_id in students:  # checks for student id in the students dictionary
        return students[student_id]
    else:
        return print('Student not found')

# Example usage
add_student(1, "Prakash")
add_student(2, "Pranav")
print(search_student(1))
remove_student(2)
print(search_student(2))