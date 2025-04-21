def count_greater_elements(arr):
    max_so_far = float('-inf')  # Start with the smallest possible number
    count = 0
    for num in arr:
        if num > max_so_far:
            count += 1
            max_so_far = num
    return count

# User input
user_input = input("Enter the array elements separated by commas: ")
arr = [int(x.strip()) for x in user_input.split(",")]  # Convert input to a list of integers

# Find and print the result
result = count_greater_elements(arr)
print("Count of elements greater than all prior elements:", result)