from collections import deque

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = 7
maze = [[0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 99, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 1]]

maze = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]


def where_am_i(r, c, n):
    for i in range(n):
        for j in range(n):
            if (i, j) == (r, c):
                print("★", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()
    print("=====================")


# (r,c)가 유효한 위치(인덱스) 인가 검사
def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


# 2차원 배열을 BFS로 탐색
def bfs(sr, sc):
    # 중복체크
    visited = [[0] * N for _ in range(N)]
    # 큐 생성
    q = deque()
    # 시작 위치 추가
    q.append((sr, sc))
    visited[sr][sc] = 1

    # 미로를 탈출할때까지 , 모든 위치를 탐색
    while q:
        # 아직 방문할 위치가 남아있다면 하나 꺼내와
        r, c = q.popleft()

        # 현재 내 위치 확인용
        where_am_i(r, c, N)

        # (r,c) 에서 해야 할일 처리
        # (r,c)가 도착점인가???
        if maze[r][c] == 99:
            print(f"탈출 : ({r},{c}) , 거리 : {visited[r][c]}")
            return True

        # (r,c)와 인접한 위치 확인
        # 인접한 위치는 상하좌우
        for d in range(4):
            # 다음 위치 계산
            nr = r + dr[d]
            nc = c + dc[d]

            # (nr,nc)가 탐색 가능한 위치인가 판별
            # 1. 배열의 범위 안(유효한 인덱스)
            # 2. 방문한적이 없어야 한다.
            # 3. 벽이 아니어야 이동할 수 있다.
            if is_valid(nr, nc) and not visited[nr][nc] and maze[nr][nc] != 1:
                # (nr,nc)는 다음에 방문
                q.append((nr, nc))
                # 중복방문 방지 + 거리 계산
                visited[nr][nc] = visited[r][c] + 1

    # 반복중에 도착지점을 찾지 못했다.
    print("탈출실패")
    return False


# bfs(0, 0)

bfs(3, 3)


def bfs2(sr, sc):
    visited = [[0] * N for _ in range(N)]

    q = deque()
    q.append((sr, sc))
    maze[sr][sc] = 1

    find = False  # 도착지점을 찾았나? 못찾았나?

    depth = 0  # 깊이 (거리)

    # 큐에 아직 남아있으면 계속 탐색
    while q:
        # 큐에서 원소를 꺼내기 전에 현재 단계에서 큐안에 방문할 원소의 개수를 미리 확인
        # 개수 만큼만 (새로 추가할거 제외) 반복을 하면 현재 단계에서 몇번 반복할지 알수 있다.
        size = len(q)

        # 깊이 1 증가
        depth += 1

        for _ in range(size):
            r, c = q.popleft()

            if maze[r][c] == 99:
                print(f"탈출 : ({r},{c}) , 거리 : {depth}")
                return True

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))

    # 반복문이 다 끝나버리면 탈출 못한거
    print("실패")
    return False