def smallest_two(arr):
    first, second = float('inf'), float('inf')
    for num in arr:
        if num < first:
            second, first = first, num
        elif num < second and num != first:
            second = num
    return first, second

arr = list(map(int, input("Enter numbers separated by space: ").split()))
smallest, second_smallest = smallest_two(arr)
print("Smallest:", smallest)
print("Second Smallest:", second_smallest)