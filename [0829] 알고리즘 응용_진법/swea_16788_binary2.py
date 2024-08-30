'''
십진수 -> 이진수

'''
import math

def dec_to_bin(dec):
    binary_number = ''

    if dec == 0:
        return '0'

    while True:
        if dec == 1:
            break

        dec = dec * 2
        binary_number = binary_number + str(math.floor(dec))
        if dec > 1:    
            dec = dec - 1


    if len(binary_number) <= 12:
        # return 0.1*len(binary_number)*float(binary_number)  
        return binary_number
    else:
        return 'overflow'

T = int(input())
for tc in range(1, T+1):
    dec_num = float(input())
    dec = dec_to_bin(dec_num)
    print(f'#{tc} {dec}')