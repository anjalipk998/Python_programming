# problem1
dict ={}
list =['a','b','c','d']
for i in range(len(list)-1):
    dict[list[i]]=(list[i],)
    
for i in sorted(dict.keys()):
    k=dict[i]
    print(k[0])

# problem2
tup =(1,2,3,4)
tup =tup[1:-1]
print(tup)
tup =tup[0]
print(tup)