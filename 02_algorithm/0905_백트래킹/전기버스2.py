# 버스 운행 하는 함수
# i : 현재위치(충전소의 인덱스)를 나타냄
# cnt : 충전횟수
def solve(i, cnt):
    global min_v

    # 내가 지금까지 cnt 번 충전했는데
    # 이전에 구한 최소값보다 크거나 같으면 이 이후에는
    # 정답이 존재할 확률이 없다. => 종료
    if cnt >= min_v:
        return

    # 종료조건
    # 도착하면 종료(정확히 마지막 정류장 OR 더가도 가능)
    if i >= N - 1:
        # 최소값 갱신
        min_v = min(cnt, min_v)
        return

    # 재귀호출
    # 현재 위치가 i일때 내가 선택 가능한 경우의 수
    # 충전용량이 bus_stop[i]
    # 내가 다음에 갈수 있는 충전소의 위치
    # 현재위치(i) + 1 <= 다음 위치(i + j) <= bus_stop[i]
    for j in range(bus_stop[i], 0, -1):
        solve(i + j, cnt + 1)


T = int(input())

for tc in range(1, T + 1):
    N, *bus_stop = list(map(int, input().split()))

    # 버스 정류장 길이 N으로 맞춰주기
    bus_stop += [0]

    # 최소 충전 횟수
    min_v = 101

    # 출발지 배터리 장착은 제외, -1
    solve(0, -1)

    print(f"#{tc} {min_v}")
