def push_zeros_to_end(arr):
    n = len(arr)
    j = 0  # Pointer for the next non-zero element

    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
print("Output:", push_zeros_to_end(arr))