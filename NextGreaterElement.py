def next_greater_element(nums1, nums2):
    stack = []
    greater_map = {}

    for num in nums2:
        while stack and stack[-1] < num:
            greater_map[stack.pop()] = num
        stack.append(num)

    return [greater_map.get(num, -1) for num in nums1]

nums1 = list(map(int, input("Enter nums1 elements separated by space: ").split()))
nums2 = list(map(int, input("Enter nums2 elements separated by space: ").split()))

print("Next greater elements:", next_greater_element(nums1, nums2))