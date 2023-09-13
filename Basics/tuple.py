empty_tuple = ()
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,
print(one_element_tuple_1)
print(one_element_tuple_2)

# access 
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-1])

for elem in my_tuple:
    print(elem)

# other methods 
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


# assignemt in left 

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

my_tuple_1 = 1, 
print(type(my_tuple_1))    # outputs: <class 'tuple'>

my_tuple_2 = 1             # This is not a tuple.
print(type(my_tuple_2))    # outputs: <class 'int'>

my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(my_tuple[3])    # outputs: [3, 4]

