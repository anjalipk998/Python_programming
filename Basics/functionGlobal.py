#global variable 
print("global variable")
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#global and local variable
print("global and local variable")
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#global keyword 
print("global keyword ")
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#global varialbe value changed
print("global varialbe value changed") 
x = "awesome"
print("Python is " + x)
def myfunc():
  global x
  x = "fantastic"
  print("inside function ::Python is " + x)

myfunc()

print("Python is " + x)