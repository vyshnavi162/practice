def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

nums = list(map(int, input("Enter the array elements separated by space: ").split()))
print("The largest sum of a subarray is:", maxSubArray(nums))