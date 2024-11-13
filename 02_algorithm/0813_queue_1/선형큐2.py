# 파이썬의 리스트 메서드를 사용해서 큐 구현

# 공백 상태의 큐
q = []

# 원소 10개 추가
for i in range(1, 11):
    q.append(i)

print(q)

# 원소 10개 삭제
for i in range(10):
    print(q.pop(0), end=" ")
print()

print(q)