from collections import Counter

def sort_by_frequency(arr):
    freq = Counter(arr)
    sorted_arr = sorted(arr, key=lambda x: (-freq[x], x))
    return sorted_arr

arr = list(map(int, input("Enter elements separated by space: ").split()))
print("Sorted by frequency:", sort_by_frequency(arr))