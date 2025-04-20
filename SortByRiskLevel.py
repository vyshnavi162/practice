def sort_by_risk_levels(arr):
    # Sort the array in ascending order
    return sorted(arr)

user_input = input("Enter the risk levels (0, 1, or 2) separated by commas: ")
arr = [int(x.strip()) for x in user_input.split(",")]  # Convert input to a list of integers

# Sort and print the result
result = sort_by_risk_levels(arr)
print("Sorted Array Based on Risk Levels:", result)