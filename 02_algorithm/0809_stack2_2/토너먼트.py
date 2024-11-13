

# i ~ j 번까지 사람들 중에서 승자를 정하고 게임 결과 정하기
def tournament(i, j):
    # 분할 : 문제를 쪼갤수 있을때까지 계속 쪼갠다
    # 쪼갤수 없으면 돌아가
    if i == j :
        # 시작과 끝이 같으면 쪼깨기 불가
        return i
    else:
        # 문제를 왼쪽부분과 오른쪽 부분으로 쪼갠다

        # 왼쪽 부분
        left = tournament(i, (i+j)//2)
        # 오른쪽 부분
        right = tournament((i+j)//2 + 1, j)

        return 왼쪽부분과 오른쪽 부분의 승자

