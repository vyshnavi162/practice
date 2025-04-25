def rotateArray(arr, k):
    n = len(arr)
    k %= n  # Handle large K values
    arr[:] = arr[-k:] + arr[:-k]  # Slice and concatenate
    return arr

arr = list(map(int, input("Enter array elements separated by space: ").split()))
k = int(input("Enter value of K (number of rotations): "))
print("Rotated Array:", rotateArray(arr, k))