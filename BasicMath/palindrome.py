'''
Palindrome Number
Batao number aage-peeche same padha jaata hai kya.
e.g. 121 -> True, 123 -> False

'''
def rev_num (int_number) -> int:
    rev = 0
    while int_number > 0:
        rev =  rev * 10 + int_number % 10
        int_number = int_number //10
        
    return rev
    
def palindrome (number):
    return rev_num(number) == number
print(palindrome(121))
         