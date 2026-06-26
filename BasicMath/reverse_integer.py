'''
Reverse a Number
Number ke digits ulta karo.
e.g. n = 1234 -> 4321
'''

def rev_integer(num):
    rev = 0
    while num >0:
        rev =  rev*10 + num%10
        num = num//10
        
    return rev
print(rev_integer(1234))
        
        
