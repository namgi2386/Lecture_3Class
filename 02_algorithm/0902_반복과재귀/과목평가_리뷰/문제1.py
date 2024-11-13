T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = input()

    # 우리가 원하는 답
    # 최대 대칭 문자열 길이
    max_length = 1

    # 대칭기준 위치 i
    # 인덱스 0과 N-1은 양옆이 없으니까 제외
    for i in range(1, N - 1):
        # i위치를 기준으로 양옆으로 한칸씩 퍼져나가 보기
        # 왼쪽으로 퍼져나가면 i-1, i-2 ...
        # 오른쪽으로 퍼져나가면 i+1, i+2 ...
        # 퍼져나가는 크기를 j 라고 하면
        # 왼쪽 최소 >= 0, 오른쪽 최대 < N
        # + 오른쪽과 왼쪽이 대칭
        # arr[i-j] == arr[i+j]
        # 두 조건을 만족하면 계속 퍼져나가면 된다.
        j = 1
        while 0 <= i - j and i + j < N and arr[i - j] == arr[i + j]:
            j += 1

        # 이반복문이 끝나면 퍼져나가는 크기 j는 최대로 커져 있을것이다.
        # (j-1)*2 + 1 => 대칭 구간의 길이
        if max_length < (j-1)*2+1:
            max_length = (j-1)*2+1

    print(f"#{tc} {max_length}")
