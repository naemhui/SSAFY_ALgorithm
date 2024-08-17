def counting_sort(data, temp):
    count = [0]*101

    for box in data:
        count[box] += 1
    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]
    for i in range(len(data)-1, -1, -1):
        count[data[i]] -= 1

        temp[count[data[i]]] = data[i]


def dump_differ(data, dump):
    for _ in range(dump):
        temp = [0] * 100 # len(data) == 100
        counting_sort(data, temp)
        data = temp

        # 평탄화
        if data[-1] - data[0] <= 1:
            break
        data[-1] -= 1
        data[0] += 1

    # 다시 정렬!!!!
    temp = [0] * len(data)
    counting_sort(data, temp)
    data = temp

    return data[-1] - data[0]


T = 10
for tc in range(1, T+1):
    dump = int(input())
    data = list(map(int, input().split()))
    count = [0]*100
    result = dump_differ(data, dump)

    print(f'#{tc} {result}')



# 1차 시도
# for i in range(dump):
#     max_v = max[height]
#     min_v = min[height]
#     height[max_v] -= 1
#     height[min_v] += 1

# while count[(-1)*i] != count[(-1)*(i+1)]:
#     while count[i] != count[i+1]
#     count[(-1)*i] -= 1
#     count[i] +=


# ## 2차 시도
# # 오류난 이유: 맨 뒤(최대), 맨 앞(최소)의 상자를 주고 받은 후 재정렬을 하지 않음!!!!
# def dump_differ(data, dump):
#     count = [0]*100
#     counting_sort(data, count)
#     i = 0
#     for _ in range(dump):
#         # 맨 뒤 최대 상자 -> 맨 앞 최소 상자 로 옮김
#         # 최소 상자 = 그 옆 자리 상자 될 때까지    
#         count[(-1)*i] -= 1  # 맨 뒤 최대 상자
#         count[i] += 1  # 맨 앞 최소 상자
#         if count[(-1)*i] == count[(-1)*(i+1)] or count[i] == count[i+1]:
#             i += 1

#         # count[i] == count[-i]
#         if i == -i + len(count):
#             break
#     max_v = max(count)
#     min_v = min(count)
#     differ = max_v - min_v
#     return differ