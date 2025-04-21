def two_sum(nums, target):
    num_map = {}  # Store number and its index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))
target = int(input("Enter the target value: "))
print("Output:", two_sum(nums, target))