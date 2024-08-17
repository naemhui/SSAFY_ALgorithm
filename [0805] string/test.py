# if t[i] == p[i]:
#     i += 1
#     j += 1
#
# else:
#     i = i-j+1
#     j = 0

p = 'TTA'
t = 'TTTTTABC'
N = len(t)
M = len(p)
cnt = 0

for i in range(N-M+1):  # 비교구간의 시작 위치
    for j in range(M):
        if t[i+j] != p[j]:
            break  # for j, 다음 글자부터 비교 시작
    else:  # for j가 중단 없이 반복되면
        cnt += 1  # 패턴 개수 1 증가

print(cnt)