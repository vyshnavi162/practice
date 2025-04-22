def sum_of_elements():
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    return sum(arr)

print("Sum:", sum_of_elements())