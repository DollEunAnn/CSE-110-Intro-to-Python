try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        print("Invalid age. Please enter a value between 0 and 120.")
    else:
        print("Your age is:", age)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

