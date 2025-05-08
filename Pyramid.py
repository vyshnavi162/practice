def print_pyramid(height, arr):
    index = 0
    for i in range(1, height + 1):
        row = []
        for _ in range(i):
            padded_num = str(arr[index]).zfill(5)  # Padding numbers with zeroes
            row.append(padded_num)
            index += 1
        print(" ".join(row))

height = int(input("Enter pyramid height: "))
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print_pyramid(height, arr)