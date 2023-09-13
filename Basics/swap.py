# using temp variable 
variable_1 = 1
variable_2 = 2


print(variable_1)
print(variable_2)

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

print(variable_1)
print(variable_2)

# with out using temp variable 
variable_1 = 1
variable_2 = 2


print(variable_1)
print(variable_2)

variable_1,variable_2=variable_2,variable_1
print(variable_1)
print(variable_2)
