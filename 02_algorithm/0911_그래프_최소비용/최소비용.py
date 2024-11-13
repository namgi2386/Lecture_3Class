from heapq import heappush, heappop

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijkstra():
    # (가중치 w, 행번호 r, 열번호 c)
    q = [(0, 0, 0)]
    # 시작 지점의 가중치는 0으로
    distance[0][0] = 0

    while q:
        # w = 가중치
        # r,c = 행번호, 열번호
        w, r, c = heappop(q)

        # 방금 꺼내온 r,c 까지의 거리 w가
        # 이전에 내가 계산해 놓은 r,c 까지의 거리보다 크면 계산 x
        if distance[r][c] < w:
            continue

        # 현재 노드와 연결되어있는 다른 인접한 노드 확인
        # 2차원 배열 => 상하좌우
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 계산한 위치가 유효한 위치면
            if 0 <= nr < N and 0 <= nc < N:
                # nr, nc 가 이동 가능한 위치
                # 연료를 1 소모해서 갈 수 있는데
                # nr,nc의 높이가 더 높으면 추가 소비
                h_diff = 0
                if arr[nr][nc] > arr[r][c]:
                    h_diff = arr[nr][nc] - arr[r][c]

                # nr,nc 까지 이동하는데 사용한 연료량
                # = r,c 까지 이동하는데 사용한 연료 + 기본 사용량(1) + 높이 차이
                # 이거랑 이전에 내가 계산해 놓은 nr,nc까지 이동하는데 사용한 연료량과 비교
                # 그중에 최소값을 선택(지금 계산한 값이 더작으면 갱신)
                cost = distance[r][c] + 1 + h_diff

                # 내가 방금 계산한 비용이 이전에 계산했던거보다 작으면 갱신
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    # 갱신이 일어났을때만 큐에 추가
                    heappush(q, (cost, nr, nc))


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # (0,0) ~ (N-1,N-1)로 가는데 최단 거리

    # distance[i] : 시작지점부터 i까지 최단 거리
    # distance[r][c] : 시작지점부터 (r,c)까지 최단 거리
    distance = [[1e9] * N for _ in range(N)]

    # 다익스트라 알고리즘 실행
    dijkstra()
    
    # (N-1, N-1) 까지의 최소 거리
    print(f"#{tc} {distance[N - 1][N - 1]}")
