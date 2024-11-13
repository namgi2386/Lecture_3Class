def inorder(t):
    global password
    # t번 노드가 존재하면
    if t < 8:
        # 왼쪽
        inorder(t * 2)
        # t번 노드에 있는 숫자 password에 이어붙이기
        password += str(bin_8[t])
        # 오른쪽
        inorder(t * 2 + 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    text = input()

    print(f"#{tc}", end=" ")
    # text에서 한글자씩 떼어와서 ord()로 아스키코드로 변환
    # 해당 아스키 코드를 이진수로 바꾸기
    for i in text:
        # 글자 하나 떼어온거 i를 아스키코드로 바꾸고
        dec = ord(i)
        # 8자리 이진수 (이따가 중위순회 할때 트리로 사용)
        bin_8 = [0] * 8

        for j in range(1, 8):
            # 숫자 1을 왼쪽으로 j번 쉬프트 해서 1이 있나 없나 비교
            # 있으면 1 붙이고, 없으면 0 붙이고
            if dec & (1 << 7 - j):  # 이렇게 하면 이따가 뒤집을 필요 없음
                bin_8[j] = 1
            else:
                bin_8[j] = 0

        # 암호화 결과 문자열
        password = ""
        # 1번부터 순회(최상위비트 제외)
        inorder(1)
        # 만든 문자열 띄어쓰고 출력
        print(password, end=" ")

    # 테스트케이스 마다 줄바꿈 한번씩
    print()
