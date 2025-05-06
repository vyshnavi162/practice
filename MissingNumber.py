def find_missing_numbers(arr, start, end):
    full_set = set(range(start, end + 1))  # Numbers in the given range
    missing_numbers = full_set - set(arr)  # Find missing numbers
    return sorted(missing_numbers) if missing_numbers else "No number is missing"

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

nums = list(map(int, input(f"Enter numbers between {start_range} and {end_range}, separated by spaces: ").split()))

print("\nOriginal array:", nums)
print("Missing number(s) in the given range:", find_missing_numbers(nums, start_range, end_range))