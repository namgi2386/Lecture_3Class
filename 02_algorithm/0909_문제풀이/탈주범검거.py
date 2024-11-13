T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 내가 가고자 하는 방향이 상 일때 갈 수 있는 터널 종류
UT = [1, 2, 5, 6]
# 내가 가고자 하는 방향이 하 일때 갈 수 있는 터널 종류
DT = [1, 2, 4, 7]
# 내가 가고자 하는 방향이 좌 일때 갈 수 있는 터널 종류
LT = [1, 3, 4, 5]
# 내가 가고자 하는 방향이 우 일때 갈 수 있는 터널 종류
RT = [1, 3, 6, 7]

U, D, L, R = 0, 1, 2, 3
# tunnel[i][j] == i번 터널에서 j방향으로 갈수있는 터널 목록
tunnel = [[],
          # 1번 터널은 상하좌우 방향 어디로든 갈 수 있음
          [UT, DT, LT, RT],
          # 2번 터널은 상하 방향 일때만 이동 가능
          [UT, DT, [], []],
          # 3번 터널은 좌우 방향 일때만 이동 가능
          [[], [], LT, RT],
          # 4번 터널은 상우 방향 일때만 이동 가능
          [UT, [], [], RT],
          # 5번 터널은 하우 방향 일때만 이동 가능
          [[], DT, [], RT],
          # 6번 터널은 하좌 방향 일때만 이동 가능
          [[], DT, LT, []],
          # 7번 터널은 상좌 방향 일때만 이동 가능
          [UT, [], LT, []]]


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < m


def bfs(r, c):
    visited = [[0] * m for _ in range(n)]
    q = []
    visited[r][c] = 1
    # 현재 위치, 현재 터널 모양 큐에 넣기
    q.append((r, c, under[r][c]))
    cnt = 1

    while q:
        # 현재 위치(r,c), 현재 터널 모양 t
        r, c, t = q.pop(0)

        if visited[r][c] >= l:
            break

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 범위, 방문, 터널
            if is_valid(nr, nc) and not visited[nr][nc] and under[nr][nc] != 0:
                # 현재 향하는 방향 d, 다음 위치의 터널 모양 체크해서 갈수 있으면 감
                nt = under[nr][nc]
                # 다음 터널 nt가 현재 터널 t에서 d방향 으로 갈수 있는 터널 목록에 있다면
                if nt in tunnel[t][d]:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc, nt))
                    # print(nr,nc)
                    cnt += 1

    return cnt


for tc in range(1, T + 1):
    # 행,열, 시작위치(행,열), 시간
    n, m, r, c, l = map(int, input().split())

    under = [list(map(int, input().split())) for _ in range(n)]

    print(f"#{tc} {bfs(r, c)}")
