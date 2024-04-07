#TSIS 5 RegEx

#ex1
import re

def check(text):
    pattern = '^ab*$'  
    if re.match(pattern, text):
        return True
    else:
        return False

text = str(input())
print(check(text))

"""
#ex2
import re

def check(text):
    pattern = '^ab{2,3}$'  
    if re.match(pattern, text):
        return True
    else:
        return False

text = str(input())
print(check(text)) 


#ex3
import re

def findseq(text):
    pattern = r'[a-z]+_[a-z]+'  
    return re.findall(pattern, text)

text = str(input())
sequences = findseq(text)
print(sequences)



#ex4
import re

def UpandLow(text):
    pattern = r'[A-Z][a-z]+'  
    return re.findall(pattern, text)

text = str(input())
sequences = UpandLow(text)
print(sequences)


#ex5
import re

def check_A_to_B(text):
    pattern = '^a.*b$'  
    if re.match(pattern, text):
        return True
    else:
        return False

text = str(input())
print(check_A_to_B(text)) 


#ex6
def replacing(text):
    return text.replace(' ', ':').replace(',', ':').replace('.', ':')

text = str(input())
new_text = replacing(text)
print(new_text)


#ex7
def S_to_C(snake):
    components = snake.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

snake = str(input())
camel = S_to_C(snake)
print(camel)


#ex8
import re

def spl(text):
    return re.findall('[A-Z][^A-Z]*', text)

text = str(input())
result = spl(text)
print(result)   

#ex9
import re

def space(text):
    return re.sub(r'(?<=[a-z])([A-Z])', r' \1', text)


text = str(input())
result = space(text)
print(result)


#ex10
import re

def C_to_S(camel_case):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel).lower()

camel = str(input())
snake = C_to_S(camel)
print(snake)

"""