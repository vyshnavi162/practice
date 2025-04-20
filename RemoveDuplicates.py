def remove_duplicates(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

user_input = input("Enter elements of the array separated by commas: ")
arr = eval(user_input)  

# Remove duplicates and print the result
result = remove_duplicates(arr)
print("Updated Array:", result)