T = int(input())

# 0 :우 , 1 :하
dr = [0, 1]
dc = [1, 0]


# 2차원 배열에서 좌표이동 할때 반드시 체크
# 움직이고 나서 2차원 배열 범위 안에 있는지
def is_vaild(r, c):
    return 0 <= r < N and 0 <= c < N


# 재귀함수로 좌표 이동하기
# 각 단계를 나타내는데 필요한 변수 (r,c) 행번호,열번호
# 숫자의 합도 매개변수로 들고 다니면 된다.
def solve(r, c, now_sum):
    global min_v
    # 가지 치기
    if min_v < now_sum:
        return

    # 종료 조건
    # 마지막 위치로 왔을때 종료
    if (r, c) == (N - 1, N - 1):
        min_v = min(min_v, now_sum)
        return

    # 재귀 호출
    # 오른쪽 or 아래
    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]
        # 다음 위치 계산 후 반드시 유효 인덱스 확인
        if is_vaild(nr, nc):
            # 갈 수 있으면 가
            solve(nr, nc, now_sum + arr[nr][nc])


for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최소값
    min_v = 13 * 13 * 10 + 1

    solve(0, 0, arr[0][0])

    print(f"#{tc} {min_v}")
