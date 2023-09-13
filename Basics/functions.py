print("------------------------------")
print("SAMPLE 1")
print("------------------------------")
def getIntput():
    print(int(input()))

print("Enter a value: ")
getIntput()

print("Enter a value: ")
getIntput()

print("Enter a value: ")
getIntput()

print("------------------------------")
print("SAMPLE 2")
print("------------------------------")

def message():
    print("Enter a value: ")
    getIntput()

print("We start here.")
message()
print("We end here.")



print("------------------------------")
print("SAMPLE 3")
print("------------------------------")


def message12():
    print("Enter a value: ")
    getIntput()


print("We start here.")
message12()
print("We end here.")


print("------------------------------")
print("SAMPLE 4")
print("------------------------------")

def hello(name):    # defining a function
    print("Hello,", name)    # body of the function


name = input("Enter your name: ")

hello(name)    # calling the function

print("------------------------------")
print("SAMPLE 5")
print("------------------------------")


def message(what, number):
    print("Enter", what, "number", number)

# invoke the function
message('Name','Anjali')
message('Age',27)

print("------------------------------")
print("SAMPLE 6")
print("------------------------------")

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")


def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

print("------------------------------")
print("SAMPLE 6")
print("------------------------------")


# Call the function here.
introduction("James", "Doe")
introduction("Henry")
introduction(first_name="William")

print("------------------------------")
print("SAMPLE 6")
print("------------------------------")


def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction()
introduction(last_name="Hopkins")
print("------------------------------")
print("SAMPLE 6")
print("------------------------------")


def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")

print("------------------------------")
print("SAMPLE 6")
print("------------------------------")
def hi(name):
    print("Hi,", name)

hi("Greg")


print("------------------------------")
print("SAMPLE 6")
print("------------------------------")

def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")

address(s, c, p_c)

print("------------------------------")
print("SAMPLE 7")
print("------------------------------")




def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    
    print("Happy New Year!")

happy_new_year()
happy_new_year(False)


print("------------------------------")
print("SAMPLE 7")
print("------------------------------")


def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned its result. It's:", x)


print("------------------------------")
print("SAMPLE 7")
print("------------------------------")


def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2))
print(strange_function(1))


print("------------------------------")
print("SAMPLE 7")
print("------------------------------")


def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

lst =[12,14]

s= list_sum(lst)

print(s)