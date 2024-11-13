T = int(input())

for tc in range(1, T + 1):
    # N : 구역 수, K : 이동 거리
    N, K = map(int, input().split())
    # 문제의 번호는 1부터 시작
    arr = [0] + list(map(int, input().split()))

    # 마지막으로 먹이를 먹은곳(위치)
    last = 1

    # 정답 (중간에 먹이를 잘 찾았으면 끝까지 갈수 있으므로 N)
    ans = N
    # 먹이를 계속 먹으면서 이동
    # 먹이를 언제까지 먹을수 있나??

    # 마지막으로 먹이를 먹은곳 + K < N ==> 계속 이동
    # 마지막 칸에 도착하지 못하면 계속 이동
    while last + K < N:
        # 마지막 위치에서 K칸 안에서 먹이가 있는지 확인
        next = last
        # last를 기준으로 last + 1 <= next <= last + K
        # 이 범위안에 먹이가 있는지 확인
        for i in range(last + 1, last + K + 1):
            # i번 위치에 먹이가 있으면
            if arr[i]:
                # 다음 위치는 i다.
                next = i

        # 반복이 끝나고 나서 next가 last 그대로 이면 먹이를 찾지 못했다.
        if next == last:
            # 마지막 먹은 위치 + K가 최대로 이동한 위치
            ans = last + K
            break

        # 중간에 먹이를 찾았으면 여기까지 실행되었다.
        last = next

    print(f"#{tc} {ans}")
