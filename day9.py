1. Right-Angled Star Triangle
*
**
***
****
def right_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)
🔹 2. Inverted Star Triangle
****
***
**
*
def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)
🔹 3. Hollow Square (this separates thinkers from typers)
****
*  *
*  *
****
def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
🔹 4. Number Pattern (1, 12, 123…)
1
12
123
1234
def number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

if __name__ == "__main__":
    n = int(input("Enter a number: "))

    print("\nRight Triangle")
    right_triangle(n)

    print("\nInverted Triangle")
    inverted_triangle(n)

    print("\nHollow Square")
    hollow_square(n)

    print("\nNumber Pattern")
    number_pattern(n)

    print("\nDone.")
