def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
print(var)
my_function()
print(var)

global var2
var2=3
print(var2)

def my_function():

    var2 = 2
    print("Do I know that variable?", var)


var2 = 1
print(var2)
my_function()
print(var)
