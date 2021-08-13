'''
3b. Write a program to convert a given number into a given base.
- Valid base is 2 <= base <= 36
- Raise exceptions similar to how int does
- Handle negative numbers just like bin and oct do.
'''

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decimal_to_base_n(decimal_num, ob):
    digits = ""
    while decimal_num:
        digits += BS[decimal_num % ob]
        decimal_num //= ob
    return digits[::-1] or "0"

def get_converted_number(num, ib, ob):
    try:
        # Convert to decimal
        if (decimal_equivalent := int(num, ib)) < 0:
            return '-' + decimal_to_base_n(abs(decimal_equivalent), ob)
        else:
            return decimal_to_base_n(decimal_equivalent, ob)
    except ValueError:
        raise ValueError("The input number doesn't match the input base") from None

input_base = int(input('Enter the input base : '))
num = input(f'Enter any number of base {input_base} : ')
output_base = int(input('Enter the output base : '))

print(get_converted_number(num, input_base, output_base))