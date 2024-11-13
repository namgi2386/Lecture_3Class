def binary_search(lst, N, key):
    # lst : 검색 대상
    # N : 검색 대상 길이
    # key : 내가 찾는 값
    start = 0  # 검색 시작 위치(인덱스)
    end = N - 1  # 검색 끝 위치(인덱스)

    while start <= end:
        # start 가 end 이하이면 제대로 된 범위 => 검색 계속
        # start 와 end가 교차 되어버리면 => 범위 잘못 => 검색 실패
        mid = (start + end) // 2  # 가운데 찍기

        if lst[mid] == key:
            # 가운데 찍었는데 원하는 값을 찾음, 검색 성공
            # 찾은 값의 위치(인덱스)를 반환
            return mid
        elif lst[mid] > key:
            # 가운데 찍었는데 원하는 값보다 크다. => 오른쪽엔 없다
            # 검색 범위를 가운데 기준 왼쪽으로 좁힌다(오른쪽은 버림)
            end = mid - 1
        else:
            # 가운데 찍었는데 원하는 값보다 작다. => 왼쪽엔 없다
            # 검색 범위를 가운데 기준 오른쪽으로 좁힌다.(왼쪽은 버림)
            start = mid + 1

    # 여기까지 왔을때 (반복문이 종료가 됬을때)
    # => 원하는 값을 찾지 못했다.
    return -1


numbers = [2, 3, 5, 7, 8, 9, 11]

print(binary_search(numbers,len(numbers),9))
print(binary_search(numbers,len(numbers),6))


