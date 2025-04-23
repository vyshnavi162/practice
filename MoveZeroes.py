def move_zeros(arr):
    non_zero = [num for num in arr if num != 0]  # Collect non-zero elements
    zeros = [0] * (len(arr) - len(non_zero))  # Create a list of zeros
    return non_zero + zeros  # Combine both lists

arr = list(map(int, input("Enter numbers separated by space: ").split()))
print("Result:", move_zeros(arr))