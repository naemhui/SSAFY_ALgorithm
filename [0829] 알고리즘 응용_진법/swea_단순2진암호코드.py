# 7비트 암호 -> 숫자값 변환
bincode_to_digit = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

# [입력]
# 가장 첫줄은 전체 테스트 케이스의 수이다.
T = int(input())
for tc in range(1, T + 1):
    # 각 테스트 케이스의 첫 줄에 두 자연수가 주어지는데
    # 각각 배열의 세로 크기 N, 배열의 가로크기 M이다 (1≤N≤50, 56≤M≤100).
    N, M = list(map(int, input().split()))
    # 그 다음 N개의 줄에 걸쳐 N x M 크기의 직사각형 배열이 주어진다.
    matrix = set(input().rstrip('0') for _ in range(N))

    result = []
    # 문자열 존재하는 줄(row) 하나만 처리하도록 로직 작성!
    for row in matrix:
        if len(row) > 0:  # 암호 코드가 있는 문자열이라면...
            # 끝에서부터 56자를 잘라준다!
            row = row[-56::]
            # 해당 암호코드를 7비트씩 "변환"해준다...! (반복문)
            for i in range(0, 56, 7):
                # 7비트 -> 숫자값 변환 (그리고 변환값 저장)
                result.append(bincode_to_digit[row[i:i + 7]])
            break
    # 암호코드 검증 로직
    # 홀수값합 * 3 + 짝수값 % 10 == 0 검증 성공!
    if ((sum(result[::2])) * 3 + sum(result[1::2])) % 10 == 0:
        print(f"#{tc} {sum(result)}")
    else:  # 검증 실패!
        print(f"#{tc} 0")