red, green, blue = input().split()

red = int(red)
green = int(green)
blue = int(blue)
total = 0

for i in range(0, red):
     for j in range(0, green):
         for k in range(0, blue):
             print(i,j,k)
             total += 1
print(total)