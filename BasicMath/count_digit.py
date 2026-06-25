'''
Count the number of digits in a given integer.
number: The integer whose digits are to be counted.
Example: number = 12345

'''

def count_number(input_number):
    count = 0
    while input_number>0:
        input_number = input_number//10
        count += 1
    return count
        
print(count_number(12345))