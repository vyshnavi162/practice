from collections import Counter

def count_frequencies():
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    return dict(Counter(arr))

print("Frequencies:", count_frequencies())