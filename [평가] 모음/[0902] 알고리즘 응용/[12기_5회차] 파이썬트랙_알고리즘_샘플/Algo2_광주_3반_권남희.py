'''
암호 생성 방법
1. 문자 -> ASCII 변환
2. 0인 최상위 비트 제외, 6~0번 비트까지 1~7번 노드에 차례로 넣기
3. 완전이진트리 중외순회 -> 그 비트열이 암호

ex. 65 -> 0100 0001
-> 맨앞 0 빼고 100 0001을 1~7 노드에 저장 (순서대로) -> 이걸 중외순회 한 순서가 암호
'''
# TypeError: ord() expected string of length 1, but list found
# print(ord('A'))

# dec = int(input())
# bin = ''
# for i in range(7, -1, -1):
#     if i & i<<2:
#         bin += '0'
#     else:
#         bin += '1'
# print(bin)

def dec_to_bin(dec):
    bin = ''
    while dec > 0:

        if dec % 2 == 0:
            bin += '0'
            dec = dec//2
            # print(dec, bin)
        else:
            bin += '1'
            dec = dec//2
            # print(dec, bin)

    if len(bin) < 8:
        bin = '0'*(8-len(bin)) + bin
        return bin
    else:
        return bin

def in_order(t):
    # cnt = 0
    if t:
        in_order(cleft[t])
        # cnt += 1
        print(bin_lst[t], end='')
        in_order(cright[t])

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 문자열의 길이
    W = input()
    arr = [1, 2, 1, 3, 2, 4, 2, 5, 3, 6, 3, 7]
    cleft = [0] * 8
    cright = [0] * 8

    for i in range(6):
        parent = arr[i * 2]
        child = arr[i * 2 + 1]
        if cleft[parent] == 0:
            cleft[parent] = child
        else:
            cright[parent] = child

    for i in range(N):
        word = ord(W[i])
        bin = dec_to_bin(word)

        bin_lst = list(bin)
        for i in range(8):
            bin_lst[i] = int(bin_lst[i])
        # print(bin_lst)

        print(f'#{tc}', end=' ')
        in_order(1)
        print()

