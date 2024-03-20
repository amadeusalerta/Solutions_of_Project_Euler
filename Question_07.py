import math

def is_prime(num):
    if (num < 2):
        return False
    elif (num == 2):
        return True
    else:
        divisible = False
        for i in range(2, int(math.sqrt(num)+1)):
            if (num%i == 0):
                divisible = True
        return not(divisible)
    
count = 2
number = 3

while count != 10001:
    number += 2
    if is_prime(number):
        count += 1

print(number)