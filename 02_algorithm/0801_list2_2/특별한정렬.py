T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    index = 0  # 바꿀 원소의 인덱스 ( 최대값 or 최소값 )

    # 앞에서부터 10개만 정렬하면 되니까 10번만
    for ni in range(10):
        # 정렬 시작, ni 인덱스 자리의 주인을 정하러 가자
        for j in range(ni, n):  # 최대값 또는 최소값을 찾기 시작
            # ni가 짝수면 큰 원소 자리
            if ni % 2 == 0 and numbers[j] > numbers[index]:
                # 최대값의 인덱스
                index = j
            # ni가 홀수면 작은 원소 자리
            if ni % 2 == 1 and numbers[j] < numbers[index]:
                # 최소값의 인덱스
                index = j

        # 현재 위치와 최대값 최소값 의 위치에 있는 원소를 자리 바꿔주기
        numbers[ni], numbers[index] = numbers[index], numbers[ni]

    # 앞에서부터 10개만 잘라서 출력
    print(f"#{tc}", *numbers[:10])