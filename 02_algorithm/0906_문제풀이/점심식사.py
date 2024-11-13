import sys

sys.stdin = open("sample_input.txt", "r")


def combination(i, s1, s2):
    if i == P:
        # 모든 사람을 두 그룹으로 나누었다면, 각각의 계단에 대해 시간을 계산
        get_time(s1, s2)
        return

    # i번 사람을 1번 계단으로
    s1.append(people[i])
    combination(i + 1, s1, s2)
    s1.pop()

    # i번 사람을 2번 계단으로
    s2.append(people[i])
    combination(i + 1, s1, s2)
    s2.pop()


def calculate_stair_time(stair, people_on_stair):
    stair_r, stair_c, stair_t = stair
    waiting_queue = []

    # 계단까지의 거리 계산
    for person_r, person_c in people_on_stair:
        distance = abs(person_r - stair_r) + abs(person_c - stair_c)
        # 계단 이용할 사람들 줄서서 기다리기
        waiting_queue.append(distance)

    # 거리가 가까운 순으로 정렬
    waiting_queue.sort()

    # 계단 내려가는 사람들
    descending_queue = []

    # 계단 앞에 도착한 사람들
    ready_queue = []

    # 걸린 시간
    time = 0

    # 사람이 셋중에 하나라도 남아있으면 계속
    while waiting_queue or ready_queue or descending_queue:
        # 계단을 내려가는 중인 사람들 시간 -1
        descending_queue = [t - 1 for t in descending_queue if t - 1 > 0]

        # 계단에 도착한 사람들 처리
        while ready_queue and len(descending_queue) < 3:
            descending_queue.append(stair_t)  # 계단 내려가기 시작
            ready_queue.pop(0)

        # 계단에 도착하지 않은 사람들의 거리 -1
        i = 0
        while i < len(waiting_queue):
            if waiting_queue[i] == 0:
                ready_queue.append(
                    waiting_queue.pop(i)
                )  # 계단에 도착하면 대기열에 추가
            else:
                waiting_queue[i] -= 1
                i += 1  # 거리 감소 후 인덱스 증가

        # 아직 사람이 남아있으면 시간증가
        if waiting_queue or ready_queue or descending_queue:
            time += 1

    return time


def get_time(s1, s2):
    global min_time

    # 1번 계단에서의 시간 계산
    s1_time = calculate_stair_time(stairs[1], s1)
    # 2번 계단에서의 시간 계산
    s2_time = calculate_stair_time(stairs[2], s2)

    # 두 계단 모두 내려가는 데 걸리는 최대 시간을 선택
    total_time = max(s1_time, s2_time)

    min_time = min(min_time, total_time)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 사람 위치
    people = []
    # 계단 위치 (계단은 두 개)
    stairs = [[]]

    # 사람과 계단 찾기
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                people.append((r, c))
            elif arr[r][c] >= 2:
                stairs.append((r, c, arr[r][c]))

    # 사람 인원 수
    P = len(people)

    # 최소 시간
    min_time = float("inf")

    # 사람을 두 집합으로 나눠보자. 모든 경우를 다 구해보자.
    # 선택 하던가 선택하지 않던가 => 조합(부분집합) 사용
    # 선택 했으면 1번 계단으로, 선택하지 않았으면 2번 계단으로
    combination(0, [], [])

    print(f"#{tc} {min_time}")
