import sys

sys.stdin = open("algo2_sample_in.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 등산로의 길이
    path = list(map(int, input().split()))  # 등산로 배열

    # 오르막의 길이 (최대) 가능한 작은값으로 초기값 설정
    max_length = 0
    # 경사도 (최소) 가능한 큰값으로 초기값 설정
    min_slope = float("inf")

    # 현재 만들고 있는 오르막의 길이
    l = 1

    start = path[0]  # 오르막의 시작 위치(높이가 제일 낮은곳)

    for i in range(1, N):
        # 현재 i위치가 오르막인가?
        # 오르막의 길이 l
        # path[i] >= path[i-1]
        if path[i] >= path[i - 1]:
            # 오르막이 이어지고 있는 중
            l += 1
        else:
            # 오르막이 끊겼다. => 오르막 하나 완성, 경사도 ,길이 계산
            # 오르막길의 조건 길이 2 이상
            if l >= 2:
                # 경사도 계산
                # 제일 높은 높이 - 제일 낮은 높이 / 경사로 길이
                slope = (path[i - 1] - start) / l

                # 현재 경사도가 제일 완만한가?
                if slope < min_slope:
                    # 이전에 내가 구했던 경사도보다 완만하면 갱신
                    min_slope = slope
                    # 길이도 갱신
                    max_length = l
                elif slope == min_slope:
                    # 현재 구한 경사도가 이전까지 알고있던 완만한 경사도와 같으면
                    # 길이가 긴것으로
                    if l > max_length:
                        max_length = l

            # 오르막길이 하나 끝났으면 다음 오르막시작
            l = 1
            start = path[i]

    # 우리가 지금 오르막을 판단하는 기준이
    # (현재 높이 > 이전 높이) 인데
    # 이 방법으론 오르막인 상태에서 배열이 끝나버리면 마지막 오르막 판단불가
    if l >= 2:
        slope = (path[-1] - start) / l
        # 현재 경사도가 제일 완만한가?
        if slope < min_slope:
            # 이전에 내가 구했던 경사도보다 완만하면 갱신
            min_slope = slope
            # 길이도 갱신
            max_length = l
        elif slope == min_slope:
            # 현재 구한 경사도가 이전까지 알고있던 완만한 경사도와 같으면
            # 길이가 긴것으로
            if l > max_length:
                max_length = l

    print(f"#{tc} {max_length}")
