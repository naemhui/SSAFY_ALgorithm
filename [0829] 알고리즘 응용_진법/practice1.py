## 아래처럼 풀어보려고 했는데 오류 : TypeError: 'int' object is not subscriptable
def bin_to_dec(bin):
    dec = 0

    if bin == '0':
        return 0

    for i in range(7):
        if bin[i] == '1':
            dec += 2**int(bin[i])
    return dec

bit = "0000000111100000011000000111100110000110000111100111100111111001100111"
"0 120 12 7 76 24 60 121 124 103"

# 이진수를 7칸씩 쪼개서 십진수로 만들기
N = len(bit)

for i in range(0,N,7):
    # i번째 비트부터 7칸 가져온 다음에 십진수로 만들기
    dec = 0  # 십진수로 바꾼 결과
    # 2^0 * bit[i+6]
    # 2^1 * bit[i+5]
    # ..
    # 2^6 * bit[i+0]
    dec = bin_to_dec(i)
    print(dec, end=" ")


########################################################
### GPT 코드
def bin_to_dec(bin_str):
    dec = 0
    length = len(bin_str)
    for i in range(length):
        if bin_str[length - i - 1] == '1':
            dec += 2**i
    return dec

bit = "0000000111100000011000000111100110000110000111100111100111111001100111"

# 이진수를 7칸씩 쪼개서 십진수로 만들기
N = len(bit)

for i in range(0, N, 7):
    bin_chunk = bit[i:i+7]
    dec = bin_to_dec(bin_chunk)
    print(dec, end=" ")
