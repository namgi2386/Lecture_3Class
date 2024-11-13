T = 10

for tc in range(1, T+1):
    n = int(input())

    buildings = list(map(int, input().split()))

    count = 0 # 조망권 개수

    for i in range(2, n-2):
        height = buildings[i] # i위치에 있는 건물의 높이
        for j in range(height, -1, -1): # 위층 부터 검사(조망권 없는 위치 나오면 그 밑은 볼 필요 없음)
            # j => 현재 층의 높이
            # 조망권 검사 조건식
            if j > buildings[i-1] and j > buildings[i-2] and j > buildings[i+1] and j > buildings[i+2]:
                count += 1
            else:
                # 만약 건물 하나라도 지금 층 보다 높으면 검사 할 필요 x
                break

    print(f"#{tc} {count}")