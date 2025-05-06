def max_product_pair(arr):
    if len(arr) < 2:
        return "No pairs exist"
    
    x, y = arr[0], arr[1]
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] * arr[j] > x * y:
                x, y = arr[i], arr[j]
    
    return x, y

nums = list(map(int, input("Enter integers separated by space: ").split()))

print("Original array:", nums)
print("Maximum product pair is:", max_product_pair(nums))