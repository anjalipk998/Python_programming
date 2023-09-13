'''
There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

Your task is to:

write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
write a line of code that removes the last element from the list (Step 2)
write a line of code that prints the length of the existing list (Step 3).
'''
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
replace_number =int(input("enter the number to be replaced:"))
# to replace the middle number with an integer number entered by the user.
middle_elem=len(hat_list)//2
print(middle_elem)
hat_list[middle_elem]=replace_number
print(hat_list)

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
# Step 3: write a line of code that prints the length of the existing list.
hat_listLength=len(hat_list)
print(hat_listLength)
print(hat_list)
