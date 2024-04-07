#TSIS 6 Built in Functions

#ex1
def multiply(num):
    result = 1
    for i in num:
        result *= i
    return result

num = []
while True:
    try:
        i = float(input())
        num.append(i)
    except ValueError:
        break

if not num:
    print("None")
else:
    result = multiply(num)
    print(f"Result: {result}")


#ex2
def count(text):
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    return upper, lower

text = str(input())
upper, lower = count(text)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")


#ex3
orig = str(input())
new = orig[::-1]

if orig == new:
    print(f"'{orig}' is palindrome")
else:
    print(f"'{orig}' is not palindrome")


#ex4
import time 
import math

def calculator(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    result = math.sqrt(number)
    return result

number = float(input())
milliseconds = float(input())

result = calculator(number, milliseconds)

print(f"Square root of {number} after {milliseconds} milliseconds is {result}")


#ex5
cortej = tuple(map(bool, input().split()))

result = all(cortej)

if result:
    print("All elements True.")
else:
    print("Not all elements  True.")
