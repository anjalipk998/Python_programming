for i in range(10):
    print("The value of i is currently", i)
print("""
-------------------------------
        next loop    
-------------------------------""")
for i in range(2,10):
    print("The value of i is currently", i)
print("""
-------------------------------
        next loop    
-------------------------------""")
for i in range(2,10,2):
    print("The value of i is currently", i)
print("""
-------------------------------
        next loop    
-------------------------------""")
for i in range(2, 8, 3):
    print("The value of i is currently", i)

print("""
-------------------------------
        next loop    
-------------------------------""")

for i in range(2, 1):
    print("The value of i is currently", i)

print("""
-------------------------------
        next loop    
-------------------------------""")
for i in range(1, 1):
    print("The value of i is currently", i)


print("power of values")

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2


for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

print()
for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

