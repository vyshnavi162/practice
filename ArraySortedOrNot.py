def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
print("Is Sorted:", is_sorted(arr))