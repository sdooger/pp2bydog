#VARIABLES

#Example 1
carname = "Volvo"


#Example 2
x = 50


#Example 3
x = 5
y = 10
print(x + y)


#Example 4
x = 5
y = 10
z = x + y
print(z)


#Example 5
x,y,z = "Orange", "Banana", "Cherry"


#Example 6
x = y = z = "Orange"


#Example 7
def myfunc():  
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)