T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    carrots = list(map(int, input().split()))

    # 당근을 3개의 박스로 나눠서 포장
    # 소, 중, 대
    # 각 상자에 담긴 당근의 개수 소 <= 중 <= 대
    # 각 상자에 담긴 당근의 차이가 최소가 되게 하려면?

    # 정렬을 하면 크기가 작은게 앞으로 오도록 할수 있겠다.
    carrots.sort()

    # 나눠 담았을때 최소 차이
    min_diff = 1000

    # 3개의 박스로 나누는 지점 두개 구하기
    # == 1 부터 N까지의 수를 쭉 나열해 놓고 그 사이 점 두개 찍기
    for i in range(1,N-1):
        for j in range(i+1,N):
            # 크기가 같은 당근은 같은 박스에 담아야 하므로
            # print(i,j)
            if carrots[i] == carrots[i-1] or carrots[j] == carrots[j-1]:
                continue

            # (소)박스에 담길 당근의 인덱스 범위 : 0 <= 소 < i  => i개
            # (중)박스에 담길 당근의 인덱스 범위 : i+1 <= 중 < j => j - i 개
            # (대)박스에 담길 당근의 인덱스 범위 : j+1 <= 대 < N => N - j 개
            # print(carrots[:i], carrots[i:j], carrots[j:],i,j)
            min_diff = min(min_diff, max(abs(j-i-i),abs((N-j)-(j-i)),abs(N-j-i)))

    if min_diff == 1000:
        min_diff = -1

    print(f"#{tc} {min_diff}")

"""
3
3
1 2 3
5
1 1 1 3 3
8
1 2 3 4 5 6 7 8
"""