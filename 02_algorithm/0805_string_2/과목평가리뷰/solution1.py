import sys

sys.stdin = open("algo1_sample_in.txt", "r")

T = int(input())

# 상하좌우
dr = [-1, 1, 0, 0]  # r(행번호)의 변화량
dc = [0, 0, -1, 1]  # c(열번호)의 변화량

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대값 (문제에서 음수가 범위에 있으므로 가능한 작은값도 음수)
    answer = -9999

    # 모든 위치에서 최대값을 구해보자. + 상하좌우(델타탐색)
    for r in range(N):
        for c in range(N):
            # 현재위치 (r,c) 에서 먹이량
            food = arr[r][c]

            # arr[r][c]+ arr[r-1][c](상) + arr[r+1][c](하) + arr[r][c-1](좌) + arr[r][c+1](우)
            # 4방향 탐색
            for d in range(4):
                nr = r + dr[d]  # 다음 행번호 = 현재행번호(r) + d방향으로 갔을때 r의 변화량
                nc = c + dc[d]  # 다음 열번호 = 연재열번호(c) + d방향으로 갔을때 c의 변화량

                # 이동할수 있는 곳인지 반드시 검사
                if 0 <= nr < N and 0 <= nc < N:
                    # 다음 위치(nr,nc)가 유효한 위치다 => 합을 구한다.
                    food += arr[nr][nc]

            # 4방향 반복이 끝난 후에 최대값 검사
            if answer < food:
                # 내가 이전에 알고있던 값보다 현재 구한 값이 더 크면
                answer = food

    print(f"#{tc} {answer}")
