def is_prime(num):
    primeFlag=False
    i=2
    while(i<=num/2):
        if(num%i==0):
            primeFlag=True
            break
        i+=1
    if primeFlag:
        return False
    else:
        return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
