T = int(input())

for tc in range(1, T + 1):
    N, D = map(int, input().split())

    # 1 ~ N 까지 꽃이 심어져 있음
    # 분무기의 범위는 D => x를 기준으로 x-D부터 x+D까지 물 뿌리기 가능(닫힌 구간: 포함)

    # N을 2*D+1로 나눠서 나머지가 0 => 몫
    # N을 2*D+1로 나눠서 나머지가 0이 아님 => 몫 + 1

    s = N // (2 * D + 1)
    r = N % (2 * D + 1)

    print(f"#{tc} {s + 1 if r else s}")

"""
3
5 1
5 2
100 3
"""