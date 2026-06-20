# Day 8: Input Validation using while loop

number = int(input("Enter a positive number: "))

while number < 0:
    print("Invalid input. Please enter a positive number.")
    number = int(input("Enter a positive number: "))

print("You entered:", number)
print("Thank you")
