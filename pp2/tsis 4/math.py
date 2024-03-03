
#TSIS 4 Math

#ex1  
import math
n = float(input())
radian = (n*math.pi)/180
print(round(radian, 6))

#ex2
height=int(input("height: "))
first=int(input("first: "))
second=int(input("second: "))
print((first+second)*(height/2))

#ex3
sides = int(input("sides: "))
length = float(input("length of a side: "))
area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))
print(area)

#ex4
length=float(input("length: "))
heigth=float(input("heigth: "))
print(float(length*heigth))

