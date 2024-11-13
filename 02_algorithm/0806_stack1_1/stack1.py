# 파이썬에서 리스트 메서드 사용해서 스택 만들기

# 1. 스택 초기화 (선언)
# 내가 이 빈 리스트를 스택으로 사용하겠다.
s = []

# 스택에 원소 삽입하기 : push
for i in range(10):
    s.append(i)

print(s)

# 스택에 원소 삭제하기 : pop
# for i in range(10):
#     print(s.pop(), end=",")
# print()
#
# print(s)

# 스택에서 원소를 모두 꺼내고 싶은데 몇개 있는지 몰라
# [] 빈리스트는 False 로 취급이 된다.
while s:
    # s 안에 뭔가가 남아있다면 아래 문장 실행
    print(s.pop(), end=" ")
print()
print(s)

