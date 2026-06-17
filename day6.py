 print("Day 6: Number Analyzer")

even_count = 0
odd_count = 0

numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\nResults:")
print("Numbers entered:", numbers)
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)

print("Thank you")
