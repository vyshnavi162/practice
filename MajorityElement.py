def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

arr = list(map(int, input("Enter elements separated by space: ").split()))
print("Majority element:", majority_element(arr))