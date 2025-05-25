def plus_one(digits):
    num = int("".join(map(str, digits)))  # Convert list to integer
    num += 1  # Increment by one
    return list(map(int, str(num)))  # Convert back to list of digits

digits = list(map(int, input("Enter digits separated by spaces: ").split()))

output = plus_one(digits)
print(f"Result: {output}")