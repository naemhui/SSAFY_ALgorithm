size = 10

cq = [0] * size
front = rear = 0

def is_full():
    return (rear + 1) % size == front

# 원형  큐에 원소 10개 삽입
for i in range(1, 11):
    if not is_full():  # 확인해야돼 근데 여기서 10 걸러질 듯
        rear = (rear + 1) % size
        cq[rear] = i

print(cq)
print(front, rear)

# 원소 size-1번 꺼내기
for i in range(9):
    front = (front + 1) % size
    print(cq[front], end = " ")
print()

print(cq)
print(front, rear)

rear = (rear + 1) % size
cq[rear] = 11

print(cq)
print(front, rear)