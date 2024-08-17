# remain = 3
# 충전count = 0
# for i in range(n):
#     remain -= 1
#     if 다음 충전기까지 거리 > remain:
#         충전 += 1
#         remain += 3
#### 내 풀이: 문제에서 제시된 테스트 케이스 3개는 맞게 나왔는데 실행 결과가 fail 뜸....
# def charging_count(k, n, stations):
#     remain = k
#     count = 0
#     position = 0
#     for i in range(1, n+1):
#         remain -= 1
#         for j in range(len(stations)-1):
#             distance = stations[i] - position
#             if distance > remain:
#                 if i == 0 or stations[j+1] - stations[j] > k:
#                     return 0
#                     count += 1
#                     remain = k - (stations[i] - stations[i - 1])
#             else:
#                 remain -= distance
#
#             position = stations[i]
#     return count
#
# T = int(input())
#
# for tc in range(T):
#     k, n, m = map(int, input().split())
#     stations = list(map(int, input().split()))
#     count = charging_count(k, n, stations)
#
#     print(f'#{tc+1} {count}')


def charging_count(k, n, stations):
    remain = k
    count = 0
    current_position = 0
    stations.append(n)  # 종점을 stations에 추가

    for i in range(len(stations)):
        distance = stations[i] - current_position
        if distance > remain:
            # 다음 충전소까지 갈 수 없는 경우
            if i == 0 or stations[i] - stations[i - 1] > k:
                return 0  # 충전 불가능한 상황
            # 이전 충전소에서 충전
            count += 1
            remain = k - (stations[i] - stations[i - 1])
        else:
            remain -= distance

        current_position = stations[i]

    return count


T = int(input())

for tc in range(T):
    k, n, m = map(int, input().split())
    stations = list(map(int, input().split()))
    count = charging_count(k, n, stations)


    print(f'#{tc + 1} {count}')
###############
# 1. 종점 처리:
#    - 첫 번째 코드는 `stations.append(n)`으로 종점을 추가했지만, 두 번째 코드는 이를 하지 않았음
#    - 이로 인해 두 번째 코드는 종점까지의 거리를 제대로 고려하지 못할 수 있음
#
# 2. 반복문 구조:
#    - 첫 번째 코드는 충전소 위치를 기준으로 반복
#    - 두 번째 코드는 모든 정류장(1부터 n까지)을 순회하며, 내부에서 다시 충전소를 확인합니다. 이는 불필요한 반복을 야기할 수 있음
#
# 3. 거리 계산:
#    - 첫 번째 코드는 `distance = stations[i] - current_position`으로 정확히 계산
#    - 두 번째 코드는 `distance = stations[i] - position`인데, 여기서 `i`는 정류장 번호여서 잘못된 계산이 될 수 있음
#
# 4. 충전 로직:
#    - 첫 번째 코드는 충전이 필요할 때 정확히 이전 충전소로 돌아가 충전
#    - 두 번째 코드는 충전 로직이 명확하지 않고, 실제로 충전을 수행하는 부분이 누락되어 있음
#
# 5. 종료 조건:
#    - 첫 번째 코드는 모든 충전소(종점 포함)를 확인한 후 종료
#    - 두 번째 코드는 n까지 모든 정류장을 순회하지만, 실제로 필요한 계산을 모두 수행하지 않을 수 있음
#
# 6. 예외 처리:
#    - 첫 번째 코드는 충전 불가능한 상황을 정확히 감지하고 0을 반환
#    - 두 번째 코드도 비슷한 로직을 시도했지만, 구현이 완전하지 않음
#
# 특히 거리 계산의 오류, 충전 로직의 누락, 그리고 종점 처리의 부재

###############
### 클로드가 만들어준 더 견고한 코드
# def charging_count(k, n, stations):
#     stations.append(n)  # 종점을 stations에 추가
#     current = 0
#     charge_count = 0
#     last_charge = 0
#
#     for i in range(len(stations)):
#         if stations[i] - current > k:
#             # 다음 충전소까지 갈 수 없는 경우
#             if i == 0 or stations[i] - stations[i - 1] > k:
#                 return 0  # 충전 불가능한 상황
#             # 이전 충전소에서 충전
#             current = stations[i - 1]
#             charge_count += 1
#             last_charge = current
#
#         if stations[i] == n:
#             # 종점에 도달했는지 확인
#             if n - last_charge <= k:
#                 return charge_count
#             else:
#                 # 마지막 충전 이후 종점까지 갈 수 없는 경우
#                 return 0
#
#     return charge_count
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     k, n, m = map(int, input().split())
#     stations = list(map(int, input().split()))
#     result = charging_count(k, n, stations)
#     print(f"#{tc} {result}")
