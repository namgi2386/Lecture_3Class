N = 3

A = [10, 20, 30]
B = [0] * N


# A를 재귀함수를 사용해서 B로 복사
# for i in range(N):
#     B[i] = A[i]

# 재귀 함수를 통해서 배열 복사
# 1. 종료 조건
# 2. 재귀 호출(종료 조건에 점점 가까이 가도록)

# 현재 복사하고 있는 인덱스 : idx
# 재귀함수 안에 필요한 값이 있다면 반드시 매개변수를 통해 전달 받기
def my_copy(idx):
    # 1. 종료 조건
    if idx == N:
        return

    # idx에서 처리할 코드들..
    B[idx] = A[idx]
    # 2. 재귀 호출
    my_copy(idx + 1)


# 0번 부터 복사 시작
my_copy(0)
print(A)
print(B)
