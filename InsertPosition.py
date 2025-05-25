def search_insert_position(nums, target):
    if target not in nums:
        return "Not there, try again!"
    
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

nums = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter target number: "))

output = search_insert_position(nums, target)
print(output)