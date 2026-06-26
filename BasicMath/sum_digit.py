'''
 Add the number of given integer
 n = 1234 -> 10 (1+2+3+4)
'''

def sum_integer(n):
    total = 0
    while n>0:
        temp = n%10
        total =  total + temp
        n=n//10
    return total

print(sum_integer(1234))