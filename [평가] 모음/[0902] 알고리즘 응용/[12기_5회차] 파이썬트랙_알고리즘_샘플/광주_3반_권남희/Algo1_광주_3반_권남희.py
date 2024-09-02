'''
1번 원소를 중심으로 대칭 -> 길이 3
길이 N, 원소 1과 0, 가장 긴 대칭 구간의 길이 찾기, 항상 홀수, 없을 경우 1
3<=T<10, 3<=N<=100
'''
# 인덱스 범위 확인
def is_possible(idx, N):
    return 0 <= idx < N

# 회문 길이 찾는 함수
def is_palindrome(word, idx, N):  # 단어, i번째 인덱스, 길이는 N
    cnt = 1  # 최소 회문 길이
    for i in range(1, N):
        nl = idx-i  # 왼쪽으로 한 칸씩 움직이며 확인
        nr = idx+i  # 오른쪽으로 한 칸씩 움직이며 확인

        if is_possible(nl, N) and is_possible(nr, N):
            if word[nl] == word[nr]:
                cnt += 2
            else:
                return cnt
        else:
            return cnt
    return cnt

### test용
# print(is_palindrome('10101', 2, 5))


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 배열의 길이
    word = input()

    max_len = 1

    # 모든 인덱스에서 회문 확인 -> 가장 큰 값 출력
    for i in range(N):
        my_cnt = is_palindrome(word, i, N)
        if my_cnt > max_len:
            max_len = my_cnt
    print(f'#{tc} {max_len}')