# Day 5: Working with lists and loops in Python

tasks = []

print("Enter 5 daily tasks:")

for i in range(1, 6):
    task = input(f"Enter task {i}: ").strip().title()
    tasks.append(task)

print("\nYour Task List:")
for task in tasks:
    print("-", task)

print("\nTotal tasks entered:", len(tasks))
print("Day 5 practice complete.")
