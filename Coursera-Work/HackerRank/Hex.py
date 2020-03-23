def print_formatted(number):
    i = 1
    while i <= number:
        hexadecimal = hex(i)[2:]
        binary = bin(i)[2:]
        n = len(bin(number)[3:])
        print(
            '{:^{width}}'.format(i,width=n), 
            '{:^{width}}'.format(oct(i)[2:],width=n), 
            '{:^{width}}'.format(hexadecimal.upper(),width=n), 
            '{:^{width}}'.format(binary,width=n)
            )
        i=i+1
print_formatted(17)

# https://pyformat.info/