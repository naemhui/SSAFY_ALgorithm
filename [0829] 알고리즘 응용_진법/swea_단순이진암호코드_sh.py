# import sys
# sys.stdin = open("input.txt", "r")

code = {
    "0001101" : 0,
    "0011001" : 1,
    "0010011" : 2,
    "0111101" : 3,
    "0100011" : 4,
    "0110001" : 5,
    "0101111" : 6,
    "0111011" : 7,
    "0110111" : 8,
    "0001011" : 9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    temp_pwd = ""

    # 암호가 있는 행 찾기
    for r in range(N):
        if int(arr[r]):  # 숫자로 바꿨을 때 1 이상이면 암호 있음
            temp_pwd = arr[r]
            break  # 모든 암호가 같으므로 뒤를 더 볼 필요가 없다

    # 우리는 이제 temp_pwd(임시)행만 보면 된다.
    # 뒤에서부터 탐색하면서 처음 1이 나오는 인덱스(마지막인덱스)를 찾자.
    # 암호의 시작 인덱스는 마지막인덱스-55다 (1~56이니까)
    # 앞뒤를 다 슬라이싱해주자
    for c in range(M-1, -1, -1):
        if temp_pwd[c]=="1":
            temp_pwd = temp_pwd[c-55:c+1]  # c까지 포함해야한다!
            break

    # 이제 진짜 암호를 찾았다. 코드와 비교해서 해독하자. 코드는 미리 최상단에 딕셔너리로 정의했다.
    istrue = 0
    result = 0
    for i in range(8):
        temp = code[temp_pwd[7*i:7*i+7]]
        result += temp

        if i%2:
            istrue += temp
        else:
            istrue += temp*3

    if istrue%10:
        result = 0

    print(f"#{tc} {result}")