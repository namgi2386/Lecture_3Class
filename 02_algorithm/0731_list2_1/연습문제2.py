import sys

sys.stdin = open("in2.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = 10  # 원소의 개수

    # 합이 0인 부분집합의 개수
    count_0 = 0

    # 집합
    number_set = list(map(int, input().split()))

    # 원소의 개수가 N개 인 집합의 부분집합의 개수는 2^N
    # 2^N번 반복해서 모든 부분집합의 합을 확인하자
    # 2^N == 1 << N
    # 시작을 1부터 하면 공집합 제외
    for i in range(1, 1 << N):
        # i번째 부분집합의 합이 0인지 확인
        ith_subset_sum = 0
        ith_subset = []

        # i를 이진수로 바꿔서 생각해보자.
        # 이진수의 각 자릿수는 0 또는 1인데
        # 1인경우 => 그 자릿수(인덱스)에 있는 원소를 골랐다고 생각하자
        # 0인경우 => 그 자릿수(인덱스)에 있는 원소를 고르지 않았다고 생각하자
        # 각 자릿수에 1이 있는지 없는지 어떻게 알아???
        # 이진수 1을 왼쪽으로 최대 N-1번 밀어 보면서 다 확인, 비트 & 연산을 사용
        # 왼쪽으로 0번밀고, 1번밀고, 2번밀고... N-1번까지 밀어보자
        for j in range(N):  # j : 왼쪽으로 밀어본 횟수
            if i & (1 << j):
                # i를 이진수로 만들었을때 j번째 비트에 1이 있다.
                # j번 원소를 i번째 부분집합에 포함한것으로 생각하겠다.
                ith_subset_sum += number_set[j]
                ith_subset.append(number_set[j])

        if ith_subset_sum == 0:
            # i번째 부분집합의 합이 0이면 1로 바꾸기(개수 구하는 문제면 +1)
            count_0 = 1
            print(ith_subset)

    print(f"#{tc} {count_0}")
