def subarraySum(nums, target):
    count = 0
    prefix_sum = 0
    prefix_map = {0: 1}
    
    for num in nums:
        prefix_sum += num
        count += prefix_map.get(prefix_sum - target, 0)
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    
    return count

nums = list(map(int, input("Enter the array elements separated by space: ").split()))
target = int(input("Enter the target sum: "))
print("Total number of subarrays with sum", target, "is:", subarraySum(nums, target))