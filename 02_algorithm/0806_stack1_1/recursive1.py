"""
1부터 10까지 출력해보기
반복문 => 재귀호출
"""
n = 10

# 시작 : 1
# 종료 : 10
# 값의 변화량 : + 1
# 값을 나타내기 위해 사용하는 변수 : i
for i in range(1, n + 1):
    print(i, end=" ")
print()


# 시작 : 1
# 종료 : 10
# 값의 변화량 : + 1
# 값을 나타내기 위해 사용하는 변수 : j
def myprint(j, n):
    # 1. 종료 조건
    if j > n:
        return

    # 2. 재귀 호출(자기 자신함수, 여기서는 myprint)
    # 필요한 작업을 수행한 후에
    print(j, end=" ")
    myprint(j + 1, n)
    # 종료 조건에 점점 가까워 지도록 재귀 호출을 해줘야한다.
    # 인자를 통해서 가까워 질수 있도록 한다.


# 재귀호출 시작
myprint(1, n)
