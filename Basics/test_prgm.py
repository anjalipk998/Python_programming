
z=0
y=10
x=y<z and z>y or y>z and z<y
print(x)

dct ={}
dct['1']=(1,2)
dct['2']=(2,1)
for x in dct.keys():
    print(dct[x][1],end="")

list4=[x*x for x in range(5)]
print(list4)
def fun(list4):
    del list4[list4[2]]
    return list4

print(fun(list4))

list1=[1,2]
for v in range(2):
    list1.insert(-1,list1[v])
    
print(list1)

lst =[i for i in range(-1,-2)]
print(lst)

print("a","b","c",sep="sep")
print("Her")