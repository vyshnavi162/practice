def mean_median(arr):
    mean = sum(arr) / len(arr)
    sorted_arr = sorted(arr)
    mid = len(sorted_arr) // 2
    median = sorted_arr[mid] if len(sorted_arr) % 2 != 0 else (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    return mean, median

arr = list(map(int, input("Enter numbers separated by space: ").split()))
mean, median = mean_median(arr)
print("Mean:", mean)
print("Median:", median)