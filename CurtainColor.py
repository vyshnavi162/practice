def max_aqua_count(colors, L):
    partitions = [colors[i::L] for i in range(L)]  # Splitting into L partitions
    max_aqua = max(partitions, key=lambda x: x.count('a'))
    return max_aqua.count('a')

colors = input("Enter curtain colors string: ")
L = int(input("Enter number of partitions (L): "))

print("Maximum aqua curtains in a box:", max_aqua_count(colors, L))