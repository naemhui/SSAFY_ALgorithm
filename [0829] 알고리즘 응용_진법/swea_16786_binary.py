'''
16진수: 0 1 2 ... 8 9 A B C D E F
'''

# 16진수 -> 10진수
def hexa_to_dec(N, hexa):
    hex_digits = '0123456789ABCDEF'
    dec_number = 0

    for i in range(N):
        dec_number += 16**i * hex_digits.find(hexa[N-1-i])

    return dec_number


def dec_to_bin(dec):
    binary_number = ""

    if dec == 0:
        return "0"

    # 0보다 클 때 2로 나누면서 나머지를 정답에 추가
    while dec > 0:
        remainder = dec % 2
        binary_number = str(remainder) + binary_number
        dec = dec // 2

    return binary_number   




T = int(input())
for tc in range(1, T+1):
    N, hexa = input().split()
    N = int(N)
    dec_number = hexa_to_dec(N, hexa)
    binary_number = dec_to_bin(dec_number)

    if len(binary_number) != N*4:
        binary_number = '0'*(N*4-len(binary_number))+binary_number

    print(f'#{tc} {binary_number}')