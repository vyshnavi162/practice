n = int(input("Enter number of elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
d = int(input("Enter number of positions to rotate: "))

rotated = arr[d:] + arr[:d]
print("Rotated array:", rotated)