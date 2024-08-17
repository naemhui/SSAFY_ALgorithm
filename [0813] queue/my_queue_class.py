N = 10
q = [0]*N
front = -1
rear = -1


rear += 1  # enq(1)
q[rear] = 1
rear += 1  #
q[rear] = 2  # enq(2)
rear +=1
q[rear] = 3
front += 1  # dequeue()
print(q[front])
front += 1  # dequeue()
print(q[front])
front += 1  # dequeue()
print(q[front])
# 위처럼 구현하면 매우 빠르게 처리 가능

# append pop은 더 느려진다.
q2 = []
q2.append(10)
q2.append(20)
print(q2.pop(0))
print(q2.pop(0))