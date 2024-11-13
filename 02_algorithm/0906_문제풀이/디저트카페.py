import sys

sys.stdin = open("sample_input.txt", "r")

# 대각선
# 왼쪽 아래 (↙)
# 오른쪽 아래 (↘)
# 오른쪽 위 (↗)
# 왼쪽 위 (↖)
dr = [1, 1, -1, -1]
dc = [-1, 1, 1, -1]


def find_path():

    # 다이아몬드 모양
    # 길이가 같은 막대기 2개가 각각 2개씩
    # 총 다이아몬드 길이 = l1 * 2 + l2 * 2 라고 볼 수 있음

    # 그럼 반을 잘라서 한쪽 길이를 total_length 라고 하자
    # 반을 잘랐을때 가능한 길이는 최대 N-1 (실제로 세어보면)
    # 최소 길이는 2

    # 최대부터 고려하면 시간 더 적게 걸리지 않을까
    for total_length in range(N - 1, 1, -1):
        # total_length = l1 + l2
        # l1과 l2는 길이 1부터 total_length -1 까지 가능
        for l1 in range(1, total_length):
            # 나머지 l2의 길이
            l2 = total_length - l1
            # 각 길이 구했으니 탐색 시작 위치 정하기
            # 다이아몬드 반절 길이가 total_length이므로
            # l1 = 왼쪽 대각선, l2 = 오른쪽 대각선 이라고 생각하면
            # 대각선 탐색 방향이 왼쪽 아래부터 가니까 l1만큼 온 상태에서 시작
            # 아래로 길이만큼 두번 간게 범위 안
            for sr in range(N - l1 - l2):
                # 대각선 왼쪽 아래부터 가니까 l1만큼 온 상태에서 시작, 오른쪽으로 l2만큼 갔을때 범위 안이여야함
                for sc in range(l1, N - l2):
                    # 디저트 번호 중복 체크
                    v = [0] * 101

                    # 탐색 시작
                    r, c = sr, sc
                    for d in range(4):
                        # 현재 방향으로 가야할 길이
                        l = l2 if d % 2 else l1
                        for _ in range(l):
                            r += dr[d]
                            c += dc[d]
                            # 먹은적 없는 디저트
                            # print(r,c)
                            if not v[MAP[r][c]]:
                                v[MAP[r][c]] = 1
                            # 먹은적 있으면 그만
                            else:
                                break
                        else:
                            # 반복 잘 돌았으면 계속
                            continue
                        # 아니면 그만
                        break
                    else:
                        # 반복 잘 돌았으면 최대 길이 완성
                        return total_length * 2

    return -1


T = int(input())

for tc in range(1, T + 1):
    # 지도 크기
    N = int(input())

    # 지도 정보 입력받기
    MAP = [list(map(int, input().split())) for _ in range(N)]

    ans = find_path()

    print(f"#{tc} {ans}")
