def decimal_to_binary(decimal):
    binary_number = ''
    if decimal == 0:
        return '0'
    while decimal > 0:
        remainder = decimal % 2
        binary_number = str(remainder)+binary_number
        decimal = decimal // 2

    return binary_number

def cnt_one(number):
    cnt = 0
    for i in range(len(number)):
        if number[i] == '1':
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    dec = int(input())
    binary_number = decimal_to_binary(dec)
    result = cnt_one(binary_number)
    print(f'#{tc} {result}')