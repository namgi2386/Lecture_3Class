T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 중간위치 (r,c) 까지 오는데 합을 다시 계산하지 않도록 기억하자
    dp = [[0] * N for _ in range(N)]
    # dp[r][c] => (r,c) 까지 오는데 최소합
    # r,c 기준 위쪽, 왼쪽 중에 최소 골라서 더하기
    for r in range(N):
        for c in range(N):
            # (r,c) 위치로 올 수 있는 방향은
            # 위에서도 올수 있고, 왼쪽에서도 올 수 있다.
            if r - 1 >= 0 and c - 1 >= 0:
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + arr[r][c]
            # 위에서만 올수 있는 경우
            elif r - 1 >= 0 and c - 1 < 0:
                dp[r][c] = dp[r - 1][c] + arr[r][c]
            # 왼쪽에서만 올수 있는 경우
            elif r - 1 < 0 and c - 1 >= 0:
                dp[r][c] = dp[r][c - 1] + arr[r][c]
            # 시작지점은(두 방향 다 불가능)
            elif r - 1 < 0 and c - 1 < 0:
                dp[r][c] = arr[r][c]

    # 반복이 다 끝나면 맨 오른쪽 아래 칸에 최소값이 있다.
    print(f"#{tc} {dp[N - 1][N - 1]}")
