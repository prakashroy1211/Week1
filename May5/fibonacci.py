def fibonacci(n):
    a, b = 0, 1
    count = 0

    print("Fibonacci sequence:")
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1

try:
    n_terms = int(input("Enter the number of terms: "))
    if n_terms <= 0:
        print("Enter a number greater than 0.")
    else:
        fibonacci(n_terms)
except ValueError:
    print("Invalid input. Please enter an integer.")