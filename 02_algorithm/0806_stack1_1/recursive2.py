"""
재귀함수를 통해 2차원 배열 행 우선 순회해보기
"""
N = 5
arr = [[N * j + i for i in range(1, N + 1)] for j in range(N)]  # 1 ~ 25

# 반복문으로 순회하면??
# 시작 ??
# 반복이 진행될 때마다 바뀌는 변수(어떤 값)??
# 종료 ??
# 1 2 3 4 5
# 6 7 8 9 10
# ...
# 21 22 23 24 25
for r in range(N):
    for c in range(N):
        print(arr[r][c], end=" ")
    print()


# 재귀함수로 순회하면??
# 시작 0,0 => 0,1 => 0,2 ...
# 1,0 => 1,1 ...
# 재귀호출이 진행될 때마다 바뀌는 변수(어떤 값)??
# 종료 4,4
def myprint(r, c, N):
    # 종료 조건
    if r == N:
        return

    print(arr[r][c], end=" ")

    # 재귀 호출(인자를 변경시켜서 종료 조건을 향해서 가도록...)
    nr, nc = r, c
    if c + 1 < N:
        nc = c + 1
    else:
        # 다음 줄로 가라.
        print()
        nc = 0
        nr = r + 1

    myprint(nr, nc, N)


myprint(0, 0, N)
