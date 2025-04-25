def singleNumber(arr):
    res = 0
    for num in arr:
        res ^= num  # XOR cancels out duplicates
    return res

arr = list(map(int, input("Enter numbers where all but one appear twice: ").split()))
print("Single Number:", singleNumber(arr))