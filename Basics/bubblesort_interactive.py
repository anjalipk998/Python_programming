my_list = []  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

length =int(input("Enter the number of elements to be sorted :"))

for i in range(length):
    my_list.append(int(input("enter the number to be appended to the list:")))
    
while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

