def findDuplicates(arr):
    res = []
    for i in range(len(arr)):
        index = abs(arr[i]) - 1
        if arr[index] < 0:
            res.append(abs(arr[i]))  # Found duplicate
        arr[index] *= -1  # Mark visited
    return res

arr = list(map(int, input("Enter elements of the array separated by space: ").split()))
print("Duplicates:", findDuplicates(arr))