# Day 3: Conditions and decision making

name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: ").strip())

if age >= 18:
    print("Hello", name)
    print("You are eligible to work and learn professional skills.")
else:
    print("Hello", name)
    print("You are not eligible yet, but keep learning!")

print("End of program.")
