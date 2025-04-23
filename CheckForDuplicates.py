def contains_duplicate(arr):
    return len(arr) != len(set(arr))  # Compare original length with unique elements length

arr = list(map(int, input("Enter array elements separated by space: ").split()))
print("Contains Duplicate?", contains_duplicate(arr))