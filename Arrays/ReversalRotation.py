def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

n = int(input("Enter number of elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
d = int(input("Enter number of positions to rotate: "))

reverse(arr, 0, d-1)
reverse(arr, d, n-1)
reverse(arr, 0, n-1)

print("Reversal rotated array:", arr)