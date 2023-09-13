#inner weroing of list
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_two) # outputs: ['bicycle', 'motor']


#slicing <list_name>[start:end] -> from start to end-1 ,arr[start:stop:step]


#copy entire list 
list3 =list_2[:]
print(list3)


# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

#using negative index

new_list = my_list[-3:-2]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)
# my_list[:end]
# my_list[0:end]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
# my_list[start:]
#  it is assumed that you want the slice to end at the element with the index len(my_list). 
# my_list[start:len(my_list)]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

# omitting both start and end makes a copy of the whole list:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

# del instruction is able to delete more than just a list's element at once - it can delete slices too:
# Note: in this case, the slice doesn't produce any new list!

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# Deleting all the elements at once is possible too:
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

# my_list = [10, 8, 6, 4, 2]
# del my_list
# print(my_list)

# in and not in operator
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

# lasrgeest from list apporach1
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)


# lasrgeest from list apporach2
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)


val =[0,1,2]
val.insert(0,1)
del val[1]
print(val)


my_list = [10, 8, 6, 4,12,43]
new_list = my_list[-5:-3]
print(new_list)
