# Day 2: Practicing user input and string operations
# Concepts used:
# - input() for taking user input
# - strip() to remove extra spaces
# - title() for formatting text
# - split() to separate first and last name
x=input("what is you name").strip().title()
z,t=x.split(" ")
print("hello",z)
y=input("please enter your adress").strip().title()
print("ypu live in ",y)
print("bye")

