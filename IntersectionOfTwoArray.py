def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

nums1 = list(map(int, input("Enter elements of first array separated by space: ").split()))
nums2 = list(map(int, input("Enter elements of second array separated by space: ").split()))

print("Intersection:", intersection(nums1, nums2))