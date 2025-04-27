def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1  # Reset count if sequence is broken

    return max_length

arr = list(map(int, input("Enter elements of the array separated by space: ").split()))

print("Length of longest continuous increasing subsequence:", longest_increasing_subsequence(arr))