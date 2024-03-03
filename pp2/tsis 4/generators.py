
#TSIS 4 Generators

#ex1
n = int(input())

for i in range(n):
    quadro = round(i**2, n)
    print(quadro)

#ex2
n = int(input())

for i in range(n):
    if i % 2 == 0 :
       print(i) 


#ex3
def divisible(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
solve = divisible(n)
for j in solve:
    print(j)

#When you use yield inside a function, it turns that function into a generator.


#ex4
n = int(input())

for i in range(n+1):
    if i >= 0:
        print(n)
        n -= 1

