import threading
import time

def print_numbers(limit):
    for i in range(limit):
        time.sleep(1)
        print("Number:", i)

def print_letters(limit):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:limit]  # Adjust the range based on user input
    for letter in letters:
        time.sleep(1)
        print("Letter:", letter)

# Getting user input for the number of iterations
num_iterations = int(input("Enter the number of iterations for numbers and letters: "))

# Creating threads with user-defined limits
thread1 = threading.Thread(target=print_numbers, args=(num_iterations,))
thread2 = threading.Thread(target=print_letters, args=(num_iterations,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads finished!")