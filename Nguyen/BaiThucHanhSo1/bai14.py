import math

x,y = map(int,input("nhap x,y").split())

d= math.sqrt(x*x + y*y)
goc = math.atan(y/x)

print(d)
print(goc)