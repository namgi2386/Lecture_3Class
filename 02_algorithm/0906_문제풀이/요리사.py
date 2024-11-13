T = int(input())


# i번 식재료를
# 음식A에 넣거나
# 음식B에 넣거나
def cook(i, A, B):
    global min_diff

    # 가지치기
    # 한쪽의 길이가 반이 넘어버리면 불가능
    if len(A) > N // 2 or len(B) > N // 2:
        return

    # 종료 조건
    # 모든 식재료를 사용했다
    if i == N:
        # A와 B의 맛 점수
        tA = tB = 0
        # i번 식재료
        for i in range(N // 2):
            # j번 식재료
            for j in range(N // 2):
                # 서로 다른 식재료면 시너지 점수 추가
                if i != j:
                    tA += ingredients[A[i]][A[j]]
                    tB += ingredients[B[i]][B[j]]

        # 최소값 구하기
        min_diff = min(min_diff, abs(tA - tB))
        return

    # 재귀 호출
    # i번 재료를 A의 재료로 사용하고 다음 재료로
    cook(i + 1, A + [i], B)
    # idx번 재료를 B의 재료로 사용하고 다음 재료로
    cook(i + 1, A, B + [i])


for tc in range(1, T + 1):
    N = int(input())

    ingredients = [list(map(int, input().split())) for _ in range(N)]

    min_diff = float("inf")

    cook(0, [], [])

    print(f"#{tc} {min_diff}")
