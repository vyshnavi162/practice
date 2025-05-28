from functools import reduce

def multiply(x, y):
    return x * y

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

product = reduce(multiply, numbers)
print("Product of all elements:", product)