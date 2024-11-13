T = int(input())

N = 0  # N극
S = 1  # S극


def 위잉치킨(o_g, o_d):
    g = o_g  # 원래 기어 번호 기억
    d = o_d  # 원래 기어 방향 기억
    l = g - 1  # g번 기준 왼쪽 기어 번호
    r = g + 1  # g번 기준 오른쪽 기어 번호

    rotate_lst = [(g, d)]  # 회전할 (기어 번호, 회전 방향) 저장, 일단 g번 기어는 무조건 회전함

    # g번 기준 왼쪽 기어 돌리기
    # g번 기어의 6번 자석과 l번 기어의 2번 자석 비교,
    while l >= 0:  # 왼쪽 기어 번호 범위
        if gears[g][6] != gears[l][2]:
            # 다르면 회전
            rotate_lst.append((l, -d))
        else:
            # 같으면 회전 안함, 반복 중단
            break
        # 회전했으면 다음 방향은 반대, 기어번호 왼쪽으로 이동, 왼쪽 기어도 왼쪽으로 이동
        d = -d
        g -= 1
        l -= 1

    g = o_g
    d = o_d
    # g번 기준 오른쪽 기어 돌리기
    # g번 기어의 2번 자석과 r번 기어의 6번 자석 비교
    while r < 4:  # 오른쪽 기어 번호 범위
        if gears[g][2] != gears[r][6]:
            # 다르면 회전
            rotate_lst.append((r, -d))
        else:
            # 같으면 회전 안함, 반복 중단
            break
        # 회전했으면 방향 반대로, 기어번호 증가, 오른쪽 기어번호도 증가
        d = -d
        g += 1
        r += 1

    for gi, di in rotate_lst:
        # gi : 회전할 기어 번호, di : 회전 방향
        if di == 1:
            # 시계방향 : 맨뒤에꺼 뽑아서 맨 앞으로 이동
            gears[gi] = [gears[gi].pop()] + gears[gi]
        else:
            # 반시계방향 : 맨앞에꺼 뽑아서 맨 뒤로 이동
            gears[gi] = gears[gi][1:] + [gears[gi].pop(0)]


for tc in range(1, T + 1):
    K = int(input())

    gears = [list(map(int, input().split())) for _ in range(4)]
    # print(gears)
    for i in range(K):
        g, d = map(int, input().split())
        g -= 1
        위잉치킨(g, d)

    score = 0
    for i in range(4):
        if gears[i][0] == S:
            score += 2 ** i

    print(f"#{tc} {score}")
