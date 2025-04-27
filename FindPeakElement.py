def findPeakElement(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left  # Index of peak element

arr = list(map(int, input("Enter elements of the array separated by space: ").split()))

print("Index of peak element:", findPeakElement(arr))