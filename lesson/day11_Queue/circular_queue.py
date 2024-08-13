Q_SIZE = 4
cQ = [0]*Q_SIZE
front = rear = 0

rear = (rear+1)%Q_SIZE  # enq(1)    # 계속 돌아가니까 out of range 오류가 안 떠서 오류 발견 힘들다
cQ[rear] = 1

rear = (rear+1)%Q_SIZE  # enq(2)
cQ[rear] = 2

rear = (rear+1)%Q_SIZE  # enq(3)
cQ[rear] = 3

front = (front+1)%Q_SIZE
print(cQ[front])

rear = (rear+1)%Q_SIZE  # enq(10)
cQ[rear] = 10

rear = (rear+1)%Q_SIZE  # enq(20)
cQ[rear] = 20

rear = (rear+1)%Q_SIZE  # enq(30)
cQ[rear] = 30