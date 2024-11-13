import random

class Node:
    def __init__(self, data):
        self.next = None  # 내 다음이 누구냐
        self.prev = None  # 내 이전이 누구냐
        self.data = data  # 내가 가진 data(아무거나)

    def __str__(self):
        return str(self.data)

class MyQ:
    # 공백 상태의 큐 생성
    def __init__(self):
        self.front = None
        self.rear = None

    # 삽입 연산
    def enq(self, node):
        # 1. 큐가 비었을때 삽입
        if self.is_empty():
            self.front = node
            self.rear = node
        # 2. 큐에 원소가 있을때 삽입
        else:
            # 현재 마지막원소의 다음 원소로 추가
            self.rear.next = node
            # 다음 원소의 이전 원소는 현재 마지막이었던 원소
            node.prev = self.rear
            # 큐의 마지막 원소를 새로운 원소를 가리키도록 바꾸기
            self.rear = node

    # 삭제 연산
    def deq(self):
        # 삭제 원소 기억
        result = self.front

        # 연결 해제 과정(front 뒤의 원소가 있을때)
        if result.next:
            # 큐의 맨앞은 front 바로 뒤의 원소가 된다.
            self.front = result.next

            # 삭제할 원소의 왼쪽과 오른쪽 연결을 해제
            result.next = None
            self.front.prev = None

        return result

    # 큐가 비었는지 확인
    def is_empty(self):
        return not self.front


q = MyQ()

# 원소 10개 삽입
for i in range(1, 11):
    num = random.randint(1,100)
    node = Node(num)
    print(num, end=" ")
    q.enq(node)
print()

# 원소 10개 삭제, 출력
for i in range(10):
    print(q.deq(), end=" ")
print()
