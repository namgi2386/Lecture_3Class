def f(i, N):    # p[i]에 서는 외계인 결정(자리 바꾸기 방법)
    global min_v
    if i == N:
        s = 0  # 현재 방법(순열)으로 줄을 세웠을때 위험도 총 합
        for i in range(1, N):
            s += arr[p[i-1]][p[i]]  # 두명 사이의 위험도
        if min_v > s:
            min_v = s

    else:
        # 자리 바꾸기 방법
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] # 위험도
    min_v = 1000    # 위험도 초기화
    p = [ i for i in range(N)]  # 외계인의 줄 선 순서

    f(0, N)
    print(f'#{tc} {min_v}')