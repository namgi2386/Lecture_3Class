# miro[i][j] == 0 : 이동 가능한 칸
# miro[i][j] == 1 : 이동 불가능한 벽
# miro[i][j] == 3 : 도착점
miro = [
    [0, 0, 0, 0, 1, 3],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
]

dr = [-1, 1, 0, 0]  # 행번호 변화량
dc = [0, 0, -1, 1]  # 열번호 변화량

n = 6


def is_vaild(r, c):
    return 0 <= r < n and 0 <= c < n


def where_am_i(r, c, n):
    for i in range(n):
        for j in range(n):
            if (i, j) == (r, c):
                print("*", end=" ")
            else:
                print(miro[i][j], end=" ")
        print()
    print("=====================")


# dfs로 2차원 배열 순회하기(미로찾기)
# 인접한 정점 == 상하좌우
# 시작 행번호 r , 시작 열번호 c
# 길이 n
def dfs(r, c, n):
    # 방문 배열
    # visited[1][1] == 1 : (1,1) 을 방문했다.
    # visited[2][2] == 0 : (2,2) 는 방문한적이 없다.
    visited = [[0] * n for _ in range(n)]
    # 스택
    stack = []
    # 시작 체크
    visited[r][c] = 1

    while True:
        # 출력용 함수
        where_am_i(r, c, n)

        # 현재 위치가 목표 위치인가 ? 판단
        if miro[r][c] == 3:
            print("도착")
            return

        # 현재 위치 (r,c)에서 방문 가능한곳 탐색
        # 상하좌우로 움직일수 있나 확인, 움직일수 있으면 가자
        for d in range(4):
            # (r,c)와 연결된 상하좌우 위치
            nr, nc = r + dr[d], c + dc[d]
            # (nr,nc)위치 이동 가능한가?
            # 1. 2차원 배열 범위 안
            # 2. 이전에 방문한적이 없다.
            # 3. 벽이 아니여야 이동 가능
            if is_vaild(nr, nc) and not visited[nr][nc] and miro[nr][nc] != 1:
                # 이 3가지 조건을 만족해야 이동 가능하다 라고 판단
                # (nr,nc)로 갈 수 있다. (r,c)를 기억하기 위해 스택에 넣기
                stack.append((r, c))
                # 방문 체크
                visited[nr][nc] = 1
                # 현재 위치를 변경
                r, c = nr, nc
                # 움직인 다음 위치에서 탐색해야 하기 때문에
                break
        # 4방향 다 봤는데 갈 수 있는 곳이 없다.
        else:
            # 내가 전에 저장했던 위치로 돌아가기
            if stack:
                r, c = stack.pop()
            else:
                break


dfs(0, 0, n)
