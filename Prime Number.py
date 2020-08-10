asa = int(input('Enter a number to check if it is a prime or not  '))
count = 0
for i in range(1, asa+1) :
    if not (asa % i) : count += 1

if (asa == 0) or (asa == 1) or (count >=3) : print(asa, "is not a prime number")
else: print (asa, "is a prime number")