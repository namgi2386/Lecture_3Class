T = int(input())


# run 또는 triple이 있는지 확인
def baby_gin(cards, counts):
    # 카드 맨앞에서 한장 뽑기
    card = card_list.pop(0)
    # 뽑은 카드 추가
    cards.append(card)
    # 카드 개수 증가
    counts[card] += 1

    # 길이가 3 이상이어야 run or triple 판단 가능
    if len(cards) >= 3:
        # run or triple 판단
        for i in range(10):
            # 트리플 인지 확인
            if counts[i] == 3:
                return True
            # 런인지 확인
            if i < 8 and counts[i] > 0 and counts[i + 1] > 0 and counts[i + 2] > 0:
                return True

    return False


for tc in range(1, T + 1):
    # 카드 리스트
    card_list = list(map(int, input().split()))
    # 플레이어1
    A = []
    # 플레이어2
    B = []

    # 플레이어1 카운트배열
    AC = [0] * 10
    # 플레이어2 카운트배열
    BC = [0] * 10

    # 승자
    winner = 0

    # 카드를 한장씩 꺼내서 나눠준 다음
    # run 또는 트리플 완성한 사람이 winner
    while card_list:
        # A가 먼저 완성했는지 보고
        if baby_gin(A, AC):
            winner = 1
            break

        # B가 완성했는지 보고
        if baby_gin(B, BC):
            winner = 2
            break

    print(f"#{tc} {winner}")
