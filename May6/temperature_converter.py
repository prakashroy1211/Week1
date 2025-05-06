def convert_temperature():
    # Display menu options to the user
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    # Ask user to choose conversion type
    choice = input("Choose conversion (1 or 2): ")

    try:
        # Prompt the user to input the temperature value
        temp = float(input("Enter temperature: "))

        # If user chooses Celsius to Fahrenheit
        if choice == '1':
            result = (temp * 9/5) + 32  # Conversion formula
            print(f"{temp}°C is {result:.2f}°F") # .2f rounds the number to two decimal places

        # If user chooses Fahrenheit to Celsius
        elif choice == '2':
            result = (temp - 32) * 5/9  # Conversion formula
            print(f"{temp}°F is {result:.2f}°C")

        # If user enters an invalid choice
        else:
            print("Invalid choice. Please select 1 or 2.")

    # Handle case where user enters something that's not a number
    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")

convert_temperature()