T = int(input())

dr = [-1, 1, 0, 0]  # 상 하 좌 우
dc = [0, 0, -1, 1]


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


# 재귀 단계 : 코어 번호
# idx : 코어 번호 , 현재 idx번 코어를 연결 할지 말지 고민중....
# connected : 전원과 연결되어 있는 코어를 기억
# board : 현재 코어를 전선과 연결한 상태를 2차원 배열로 기억
# l : 현재까지 연결한 전선의 길이
def solve(idx, l, connected, MAP):
    global max_core_cnt, min_line_length

    # 0. 가지치기
    # 남은 코어 개수 다 더해도 최대 코어 개수보다 작으면 진행 중단
    if len(connected) + len(core_list) - idx < max_core_cnt:
        return

    # 1. 종료 조건
    if idx == len(core_list):
        # 모든 코어를 다 고려했다. (어떻게 연결할지)
        # 코어 개수 갱신
        if max_core_cnt < len(connected):
            max_core_cnt = len(connected)
            min_line_length = l
        # 최대 코어 개수 많으면 전선 길이 짧은걸로
        elif max_core_cnt == len(connected):
            min_line_length = min(l, min_line_length)
        return

    # 2. 재귀 호출
    # 현재 idx번째 코어의 위치
    r, c = core_list[idx]

    if (r, c) in connected:
        # 이미 전류가 흐르고 있으면 생각할 필요 없이 바로 다음 코어로
        solve(idx + 1, l, connected, MAP)
    else:
        # 연결 안되어 있으면 4방향 중에 하나 골라서 연결해보고 다음 코어로
        for d in range(4):
            nr, nc = r, c
            # d 방향으로 연결한 전선들의 위치를 기억
            temp_list = []
            # d 방향으로 연결 가능 하면 위에 temp_list 안에 있는 위치에 전선 놓고 다음 코어로
            can_connect = True

            # d방향으로 계속 뻗어나가 보기
            while True:
                nr += dr[d]
                nc += dc[d]
                if not is_valid(nr, nc):  # 다음 위치가 외곽. 중간에 전선or 코어 없음 => 이 방향으로 연결 가능
                    break
                if MAP[nr][nc] != 0:
                    # 중간에 다른 뭔가가 있으면 이 방향은 연결 불가
                    can_connect = False
                    # 뻗어나가기 그만
                    break
                # 현재 (nr,nc) 위치에 전선을 놓겠다.
                temp_list.append((nr, nc))

            # d 방향으로 연결이 가능했다
            if can_connect:
                # temp_list 안에 있는 전선 위치에 전선 놓고 다음 코어로(재귀호출)
                for (vr, vc) in temp_list:
                    MAP[vr][vc] = 2  # 전선 표시

                # 다음 코어로(idx+1), 전선 길이만큼 더하고, 현재 위치에 있는 코어 연결완료
                solve(idx + 1, l + len(temp_list), connected + [(r, c)], MAP)

                # 되돌리기
                # d 방향으로 연결했던 전선을 모두 제거하고 다른 방향도 고려
                for (vr, vc) in temp_list:
                    MAP[vr][vc] = 0  # 전선 제거

        # 원래 전류가 흐르지 않은 코어였더라도 이 코어에 연결은 안하는 상황 포함
        solve(idx + 1, l, connected, MAP)


results = []

for tc in range(1, T + 1):
    N = int(input())

    # 초기 코어의 배치 상태
    MAP = [list(map(int, input().split())) for _ in range(N)]

    # 최대 코어 개수
    max_core_cnt = 0
    # 최대 코어를 연결 했을때 전선 길이(경우가 여러개라면 그중에 최소)
    min_line_length = N * N
    # 코어 위치 모음
    core_list = []
    # 전류가 흐르는 위치를 기억하기 위한 배열
    connected_list = []

    # 주어진 2차원 배열을 쭉 순회 하면서 코어 위치만 모으기
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1:
                # 코어 위치 추가
                core_list.append((i, j))
                # 가장자리에 코어가 있다면 거기는 이미 전류가 흐르는 위치
                if i == 0 or j == 0 or i == N - 1 or j == N - 1:
                    connected_list.append((i, j))

    # 재귀함수 호출
    solve(0, 0, connected_list, MAP)

    results.append(f"#{tc} {min_line_length}")

# 모든 테케 결과 출력 1번만
print("\n".join(results))
