T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def check_possible():
    for i in range(N):
        for j in range(M):
            # 색이 흰색(".")이나 검정색("#")으로 이미 칠해져 있는 경우
            if A[i][j] != "?":
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    # 한 변을 공유한다 => 상하좌우
                    # 상하좌우에 나랑 같은 색이 이미 칠해져 있으면 impossible
                    if 0 <= ni < N and 0 <= nj < M and A[ni][nj] == A[i][j]:
                        return "impossible"

            # 색이 아직 안정해진("?") 경우
            else:
                # 인접한 칸에 있는 검은색 격자 수
                B = 0
                # 인접한 칸에 있는 흰색 격자 수
                W = 0

                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0 <= ni < N and 0 <= nj < M:
                        if A[ni][nj] == ".":
                            W += 1
                        # ? 일수도 있으니 else는 쓰면 안됨
                        elif A[ni][nj] == "#":
                            B += 1

                # 1. 상하좌우에 칠해진 색이 없음 => 일단 두고 진행
                if B + W == 0:
                    continue
                # 2. 상하좌우에 칠해진 색이 있음
                # 2-1. 서로 다른 색 있으면 => impossible
                elif B > 0 and W > 0:
                    return "impossible"
                # 2-2. 색이 모두 같음 => 다른색으로 색칠하고 진행
                elif B > 0 and W == 0:
                    # 주변에 검정색만 있으니 흰색으로 칠하고 진행
                    A[i][j] = "."
                elif W > 0 and B == 0:
                    # 주변에 흰색만 있으니 검정색으로 칠하고 진행
                    A[i][j] = "#"

    # 중간에 불가능한 경우를 만나지 않고 여기까지 실행되면 possible
    return "possible"


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    A = [list(input()) for _ in range(N)]

    print(f"#{tc} {check_possible()}")

"""

3
3 6
#.????
?#????
???.??
1 6
##????
3 3
.#.
#?#
.#.
"""