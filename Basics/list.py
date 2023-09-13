numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("New list content: ", numbers)  # Current list content.

# copying elemetns 


numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list content:", numbers)  # Printing current list content.
print(numbers[0]) # Accessing the list's first element.
print(numbers)  # Printing the whole list.
print("\nList length:", len(numbers))  # Printing the list's length.
###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.
# print(numbers[4]) 
# numbers[4] = 1
###

# negative index 
numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])

###
#add values using append 
numbers.append(4)

print(len(numbers))
print(numbers)

###
#add values using insert
numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
numbers.insert(1, 333)
print(len(numbers))
print(numbers)


my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)


my_list1 = []  # Creating an empty list.

for j in range(5):
    my_list1.insert(0, j + 1)

print(my_list1)


my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)


my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
    

my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]

del my_list  # deletes the whole list

my_list = ["white", "purple", "blue", "yellow", "green"]

for color in my_list:
    print(color,end=' ')
print()
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))

lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)



my_list = [52,78,10,12,20,2]
print(my_list)
my_list.reverse()
print(my_list)
my_list.sort()
print(my_list)

lst = ["D", "F", "A", "Z"]
lst.sort()

print(lst)

a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()

print(lst)

a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()

print(lst)