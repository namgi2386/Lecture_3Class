T = int(input())

#  0  1  2  3
#  우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())  # 달팽이 크기

    snail = [[0] * N for _ in range(N)]

    # 방향 (오른쪽부터 시작하니까 0)
    d = 0
    # 현재 위치 (0,0)에서 시작
    r, c = 0, 0

    for i in range(1, N * N + 1):
        snail[r][c] = i

        # 방향을 언제 바꿔야 할까??

        # 다음 위치를 일단 계산 해서
        # 배열의 범위를 벗어났을때
        # 내가 이전에 놓은 숫자를 만났을때

        # 방향 바꿨으면 다음 위치 다시 계산

        nr = r + dr[d]  # 다음 행 번호(인덱스)
        nc = c + dc[d]  # 다음 열 번호(인덱스)

        # 다음 위치로 갈수 있는가?? (유효한 인덱스인가)
        # 다음 위치에 내가 이전에 놓은 숫자가 있어도(0이 아니면) 가면 안된다.
        # 갈수있으면 가면된다. r,c = nr,nc
        if 0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0:
            # 다음 위치 갈수 있으면 그대로 진행
            r, c = nr, nc
        else:
            # 다음 위치가 유효한 인덱스가 아니면 범위를 벗어났거나
            # 내가 이전에 이미 숫자를 놓은적이 있던가

            d = d + 1 if d < 3 else 0

            # if d + 1 < 3:
            #     d += 1
            # else:
            #     d = 0

            # d = (d+1)%4

            # 방향 바꾸고 다시 계산
            r = r + dr[d]
            c = c + dc[d]

    print(f"#{tc}")

    # for r in range(N):
    #     for c in range(N):
    #         print(snail[r][c], end=" ")
    #     print()

    for r in range(N):
        print(*snail[r])
