import sys

sys.stdin = open("in.txt", "r")

# 델타 배열
# 상 > 하 > 좌 > 우
# 0   1    2    3
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


# 좌표 검사 함수
def is_valid(i, j):
    return 0 <= i < N and 0 <= j < N


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 모든 위치를 탐색 하면서
    # 모든 위치에서 상하좌우 원소를 가져온 다음에 차의 절댓값 구하기

    # 모든 위치의 절댓값 합
    diff_sum = 0
    for i in range(N):
        for j in range(N):
            # 행번호 i, 열번호 j
            # (i,j) 위치에서 상하좌우 차이 (절댓값)구하기
            # (i,j) 위치에서 절댓값 합
            now_diff_sum = 0

            for d in range(4):
                ni = i + di[d] # 현재 위치 i에서 d 방향으로 갔을때 i의 변화량
                nj = j + dj[d] # 현재 위치 j에서 d 방향으로 갔을때 j의 변화량

                # 우리가 계산한 다음 위치가 유효한 인덱스인지 반드시 검사
                if is_valid(ni,nj):
                # if 0<= ni < N and 0<= nj < N:
                    diff = arr[i][j] - arr[ni][nj]
                    
                    # 우리가 원하는건 절댓값, 음수면 부호 바꿔주기
                    if diff < 0:
                        diff = -diff

                    # ni, nj가 유효한 위치일때 절댓값 합 더해주기
                    now_diff_sum += diff

            # 상하좌우 탐색이 끝난 후에 현재 위치 절대값 차이 합 더해주기
            diff_sum += now_diff_sum

    print(f"#{tc} {diff_sum}")
