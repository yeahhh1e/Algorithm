N = 10
q = [0] * N
front = rear = -1

rear += 1   # enqueue(1)
q[rear] = 1
rear += 1
q[rear] = 2 # enqueue(2)
rear += 1   # enqueue(3)
q[rear] = 3

front += 1 # dequeue()
print(q[front]) # 1
front += 1 # dequeue()
print(q[front]) # 2
front += 1 # dequeue()
print(q[front]) # 3


q2 = []
q2.append(10)
q2.append(20)
print(q2.pop(0))    # 10
print(q2.pop(0))    # 20

