dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


# r,c : 현재 위치
# l : 길이
# h : 현재 높이
# cut : 지형 깎기 기회 여부
# load : 지금까지 만든 등산로, 중복체크용
def solve(r, c, l, h, cut, load):
    global max_l
    # 어차피 언젠간 끝나 그냥 최댓값 계산 길 생길때마다 해버리자
    max_l = max(max_l, l)

    # 4방향 탐색 후 길이 있으면 거기로 가고 길이 없으면 깎아서 간다
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        # 갈수 있고 이전에 간적 없으면 간다
        if is_valid(nr, nc) and (nr, nc) not in load:
            # 다음 위치의 높이가 현재 높이보다 작으면 오케이
            if arr[nr][nc] < h:
                load.append((nr, nc))
                solve(nr, nc, l + 1, arr[nr][nc], cut, load)
                load.pop()
            # 나랑 같거나 나보다 높아도 깎을 기회 남아 있다면 오케이
            elif cut:
                # 이제 깎을껀데 1 부터 k 까지 깎을수 있음
                for nh in range(arr[nr][nc] - k, arr[nr][nc]):
                    # 깎은 높이 나보다 작으면 오케이
                    if nh < h:
                        load.append((nr, nc))
                        solve(nr, nc, l + 1, nh, 0, load)
                        load.pop()


T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    max_h = 0
    start_list = []
    # 등산로는 가장 높은 봉우리(여러개) 에서 시작
    for i in range(n):
        for j in range(n):
            if max_h < arr[i][j]:
                start_list = [(i, j)]
                max_h = arr[i][j]
            elif max_h == arr[i][j]:
                start_list.append((i, j))

    # 조건을 만족하는 가장 긴 등산로
    max_l = 0
    # 등산로 조성 시작
    for r, c in start_list:
        # print(arr[r][c])
        solve(r, c, 1, max_h, 1, [(r, c)])

    print(f"#{tc} {max_l}")
