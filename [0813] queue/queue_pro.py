size = 10

# 공백 상태의 큐 생성
q = [0]*size

front = rear = -1
# front: 첫 원소의 위치 (다음에 삭제될 원소)
# rear : 마지막 원소의 위치

for i in range(1, 11):
    # 삽입 전에 rear + 1
    rear += 1
    # +1한 위치에 원소를 넣는다
    q[rear] = i

print(q)
print(front, rear)

# 원소 10개 삭제해보기
for i in range(10):
    # 삭제 전에 front +1
    front += 1
    # +1 한 위치에 있는 원소를 사용(삭제)
    print(q[front], end = " ")
print()

print(q)
print(front, rear)