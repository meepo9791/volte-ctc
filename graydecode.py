def Graytobinary(n):
    n = int(n, 2)
    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask
    return bin(n)[2:]

binary_val= input('Enter the graycode number: ')
print('binary is:', Graytobinary(binary_val))