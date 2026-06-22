#1
def count_numbers(nums):
    pos = neg = zero = 0

    for n in nums:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        else:
            zero += 1

    return pos, neg, zero
#2
def find_max_min(nums):
    largest = nums[0]
    smallest = nums[0]

    for n in nums:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n

    return largest, smallest
#3
def reverse_list(nums):
    reversed_list = []
    for i in range(len(nums) - 1, -1, -1):
        reversed_list.append(nums[i])
    return reversed_list
#4
def remove_duplicates(nums):
    unique = []
    for n in nums:
        if n not in unique:
            unique.append(n)
    return unique
#5


if __name__ == "__main__":
    nums = []

    size = int(input("Enter number of elements: "))
    for i in range(size):
        nums.append(int(input(f"Enter element {i+1}: ")))

    print("\nOriginal list:", nums)

    pos, neg, zero = count_numbers(nums)
    print("Positive:", pos, "Negative:", neg, "Zero:", zero)

    largest, smallest = find_max_min(nums)
    print("Largest:", largest)
    print("Smallest:", smallest)

    print("Reversed list:", reverse_list(nums))
    print("Without duplicates:", remove_duplicates(nums))

    print("\nDay 10 complete.")
