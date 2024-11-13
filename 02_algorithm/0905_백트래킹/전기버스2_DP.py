T = int(input())

for tc in range(1, T + 1):
    N, *bus_stop = map(int, input().split())

    # 중복 계산을 방지하기 위해
    # 내가 중간에 계산한 값을 저장한다.
    DP = [99999] * [N]
    # DP[i] = i번 까지 가는데 최소 충전 횟수
    DP[0] = 0

    # 모든 위치에서 충전해보고 이전에 계산한적이 없으면 계산
    for i in range(1, N):
        # 위치 i까지 오는데 최소 충전 횟수??
        # i에 오기 전위치 j
        # j + bus_stop[j] >= i 이면 i에 올 수 있다.
        # i까지 오는데 최소 충전 횟수 = j까지 오는데 최소 충전횟수 + 1
        # 이전에 다른 j에서 왔던 횟수와 비교해서 최소값만 저장
        for j in range(i):
            if j + bus_stop[j] >= i:  # j에서 i로 이동 가능했다.
                DP[i] = min(DP[i], DP[j] + 1)

    # 반복문이 끝나면 DP의 마지막 값에 최소 충전 횟수가 있다.
    print(f"#{tc} {DP[N - 1] - 1}")
