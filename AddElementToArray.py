def add_element(arr, element):
    arr.append(element)  # Append the element to the array
    return arr

arr = list(map(int, input("Enter array elements separated by space: ").split()))
element = int(input("Enter the element to add: "))
print("Updated Array:", add_element(arr, element))