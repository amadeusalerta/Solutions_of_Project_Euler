x = 1
y = 1
z = 0
result = 0

while z < 4000000:
   z = (x+y)         
   if z%2 == 0:
       result = result + z
       
   x = y
   y = z

print (result)

#The Answer is 4613732