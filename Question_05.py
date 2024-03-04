def smallest_evenly_divisible():
    number = 1
    while True:
        if all(number % n == 0 for n in range(2, 21)):
            return number
        number += 1

print(smallest_evenly_divisible())