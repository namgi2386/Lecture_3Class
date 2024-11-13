T = int(input())

# idx : 교환 횟수
def find_max(idx):
    global answer
    # 0. 가지 치기
    # 내가 이전에 idx번 써서 현재 숫자 만든적 있으면 더 진행할 필요 xxx
    now_num = int("".join(nums))

    if (idx, now_num) in visited:
        # 더이상 진행 불가
        return

    # idx번 써서 현재 숫자 만든적 없으면 중복 체크 하고 진행
    visited.add((idx, now_num))

    # 1. 종료 조건
    if idx == cnt:  # 교환 횟수 다 사용 했으면 그만(재귀호출 중지)
        # 최대 상금 갱신
        answer = max(answer, now_num)
        return

    # 2. 재귀 호출
    # idx번 바꾸는 상황에서 자리를 바꿀 두 원소의 위치를 정해줘야 한다.
    # i : 바꿀 숫자 중에 앞쪽 숫자의 위치 0 <= i < N-1 (뒤에 최소 1개는 남아있음)
    # j : 바꿀 숫자 중에 뒷쪽 숫자의 위치 i+1 <= j < N (앞에 최소 1개는 남아있음)
    for i in range(N - 1):
        for j in range(i + 1, N):
            # 자기 자신을 바꾸는 경우는 없음
            nums[i], nums[j] = nums[j], nums[i]
            # 다음 횟수로 진행
            find_max(idx + 1)

            # 자리 바꿨던 일 없던 일로 원상복귀
            nums[i], nums[j] = nums[j], nums[i]


for tc in range(1, T + 1):
    nums, cnt = input().split()
    # 숫자 카드
    nums = list(nums)
    # 교환 횟수
    cnt = int(cnt)
    # 숫자 개수
    N = len(nums)

    visited = set()
    # (1, 141414) => 교환 1번 해서 141414 만든적 있다.
    # 뒤에서 교환1번 해서 141414 만든 경우는 더이상 진행하지 않아도 된다.

    # 최대 상금
    answer = 0

    find_max(0)
    print(f"#{tc} {answer}")

"""
3
123 1
2737 1
32888 2
"""
