'''
Write a function which takes two integers num1 and num2 and returns 1
 if there is a straight triple of a digit at any place in num1
  and also a straight double of the same digit in num2.

If this isn't the case, return 0.

Examples
451999277, 41177722899 -->  1 // num1 has straight triple 999s and num2 has straight double 99s
1222345, 12345 -->  0 // num1 has straight triple 2s but num2 has only a single 2
12345, 12345 -->  0
888, 77 --> 0 // num1 has three '8's, num2 has 2 '7's, but they are not the same digit
88888, 88888   --> 1 // more than 3 or 2 repetitions also count
123123123, 123 --> 0 // '123' is not a single digit

'''

def triple_double(num1, num2):
    # Convert numbers to strings to iterate over digits
    str_num1 = str(num1)
    str_num2 = str(num2)

    # Check for a straight triple in num1
    for i in range(len(str_num1) - 2):
        if str_num1[i] == str_num1[i + 1] == str_num1[i + 2]:
            # If a triple is found, check for a double in num2
            if str_num1[i] * 2 in str_num2:
                return 1
    return 0

def triple_double(num1, num2):
    return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])


print(triple_double(451999277, 41177722899))
print(triple_double(1222345, 12345))