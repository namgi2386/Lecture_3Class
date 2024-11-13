def counting_sort(DATA, TEMP, K):
    # DATA : 정렬 대상(배열)
    # TEMP : 정렬 결과(배열)
    # K : 정렬 대상 중 최댓값 = 카운트 배열의 크기
    COUNT = [0] * (K + 1)
    # COUNT : 카운트 배열(등장하는 원소의 개수를 세기 위해)
    # C[X] = X의 등장 횟수
    # C[1] => DATA 안에 1이 몇개 있는가를 말해준다.

    # 1. 각 원소의 등장 횟수를 카운트
    for num in DATA:
        # DATA 배열 안에서 꺼내온 숫자 num의 등장 횟수 + 1
        COUNT[num] += 1

    # 2. 각 원소의 등장횟수를 계산해서 각 원소가 들어갈 자리 위치를 계산
    # 내 앞자리(나보다 작은원소들의 개수) + 현재 나의 등장 횟수 ... 누적
    for i in range(1, len(COUNT)):
        COUNT[i] = COUNT[i] + COUNT[i - 1]

    # 3. 뒤에서부터 DATA를 확인하면서 COUNT를 보고 자리를 확인
    # COUNT의 숫자 - 1 하고 그 위치에 넣는다.
    # 뒤에서 확인하는 이유는 안정 정렬(원래 순서 보장)
    for i in range(len(DATA) - 1, -1, -1):
        # 자리에 놓기 전에 -1 (자리 겹치는거 방지)
        # DATA[i]번째 친구의 자리 번호
        COUNT[DATA[i]] -= 1

        # COUNT[DATA[i]] => DATA[i] 원소가 들어갈 자리번호(인덱스)
        TEMP[COUNT[DATA[i]]] = DATA[i]


nums = [0, 4, 1, 3, 1, 2, 4, 1]  # 원본
result = [0] * 8  # 정렬 결과

counting_sort(nums, result, max(nums))
print(result)
