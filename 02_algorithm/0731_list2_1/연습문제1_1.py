import sys

sys.stdin = open("in.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 대각의 합
    dia_sum = 0
    # 대각선 좌표??
    for i in range(N):
        for j in range(N):
            # 오른쪽 아래 대각선??
            if i == j:
                dia_sum += arr[i][j]
            # 왼쪽 아래 대각선??
            if N-1-i == j:
                dia_sum += arr[i][j]
    
    # 겹치는 부분 빼주기
    dia_sum -= arr[N//2][N//2]
    print(dia_sum)