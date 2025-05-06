from array import array

nums = list(map(int, input("Enter 6 integers separated by space: ").split()))

if len(nums) != 6:
    print("Please enter exactly 6 integers.")
else:
    my_array = array('i', nums)

    for num in my_array:
        print(num)