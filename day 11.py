#1
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
#2
def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
#3
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
#4
def fibonacci(n):
    series = []
    a, b = 0, 1

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series
#5
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Is prime:", is_prime(num))
    print("Factorial:", factorial(num))

    start = int(input("\nEnter range start: "))
    end = int(input("Enter range end: "))
    print("Primes in range:", primes_in_range(start, end))

    terms = int(input("\nEnter Fibonacci terms: "))
    print("Fibonacci series:", fibonacci(terms))

    print("\nDay 11 complete.")
