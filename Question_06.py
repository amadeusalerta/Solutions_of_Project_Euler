square = 0
parant = 0

for i in range(1, 101):
    square += i**2
    parant += i

parant = parant**2

print(parant - square)