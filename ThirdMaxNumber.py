def third_max(arr):
    first, second, third = float('-inf'), float('-inf'), float('-inf')
    for num in arr:
        if num > first:
            third, second, first = second, first, num
        elif num > second and num != first:
            third, second = second, num
        elif num > third and num != second and num != first:
            third = num
    return third if third != float('-inf') else None

arr = list(map(int, input("Enter numbers separated by space: ").split()))
third_max_num = third_max(arr)
print("Third Maximum:", third_max_num if third_max_num is not None else "Not enough unique numbers.")
