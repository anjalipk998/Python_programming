'''
 find the location of a given element inside a list:
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False


for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

'''Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49.

The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.

The question is: how many numbers have you hit?
'''
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

'''
magine a list - not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.

Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.
'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
i=0
while True:
    num = my_list[i]
    if (my_list.count(num)>1):
        my_list.remove(num)
        my_list.append(num)
    length=len(my_list)
    i+=1
    if(i>=length):
        break
print("The list with unique elements only:")
print(my_list)
