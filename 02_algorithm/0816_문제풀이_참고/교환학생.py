T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    A = list(map(int, input().split()))

    # 대학교에 있어야 하는 최소 일 수
    min_d = 99999999

    # 모든 에서 시작 해서 최소값 구해보기
    # 시작 요일을 s라고 하자
    for s in range(7):
        # 수업 들은 횟수 cnt 가 N 될때 까지 반복
        cnt = 0
        # 총 경과한 날짜
        d = 0

        if not A[s]:
            # 시작 일에 수업 없으면 어차피 최소 안돼 건너 뛰어
            continue

        # 수업 다 들을때까지
        while cnt != N:
            # s 요일에 수업이 있으면
            if A[s]:
                # 수업 들은 횟수 증가
                cnt += 1
            # 요일 + 1 증가, 일주일 끝나면 다시 일요일부터 시작
            s = (s + 1) % 7

            # 하루 경과
            d += 1

        # s요일에서 시작해서 다 들었으면 최소값 비교
        min_d = min(d, min_d)

    print(f"#{tc} {min_d}")

"""

5
2
0 1 0 0 0 0 0
100000
1 0 0 0 1 0 1
1
1 0 0 0 0 0 0
7
0 1 1 1 0 0 0
2
1 0 0 0 0 0 1

"""