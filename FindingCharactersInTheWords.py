def find_indices(words, x):
    return [i for i in range(len(words)) if x in words[i]]

words = input("Enter words separated by spaces: ").split()
x = input("Enter the character to search for: ")

print("Indices of words containing", x, ":", find_indices(words, x))