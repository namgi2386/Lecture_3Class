T = int(input())

for tc in range(1, T + 1):
    # N : 한 변의 길이(글자 길이)
    # M : 우리가 찾는 회문의 길이
    N, M = map(int, input().split())

    text = [list(input()) for _ in range(N)]

    result = ""  # 정답이 될 문자열

    # 모든 위치 (i,j) 에서 회문을 만들기 시작해보자.
    for i in range(N):
        for j in range(N - M + 1):  # j는 회문을 만들수 있는 시작 위치만 반복
            # 전체 길이 - 회문 길이 + 1 (인덱스)
            # (i,j) 여기 있는 글자가 회문의 첫글자
            # (i,j+0) (i,j+1) //(i,j+2).. (i,j+4)
            # is_p = True # 회문이 된다.
            for k in range(M // 2):  # 회문은 반으로 쪼갰을때 앞에 부분까지만 뒤집어보면 알수 있다.
                if text[i][j + k] != text[i][j + M - 1 - k]:
                    # is_p = False # 회문안된다.
                    # 회문 시작 좌표(i,j+k) , 회문 끝 좌표(i,j+M-1-k)
                    break
            else:
                # 중간에 반복문이 중단된적이 없으면 실행해라.
                # (i,j) 에서 길이 M짜리 회문 검사했는데
                # 중간에 회문안된다는 조건을 만난적이 없음(중단된적이없다.)
                result = "".join(text[i][j: j + M])

            # 세로로 검사
            for k in range(M//2):
                if text[j + k][i] != text[j + M - k - 1][i]:
                    break
            else:
                # 고수용
                # zip()을 통해 가로<->세로 뒤집고 슬라이싱
                result = "".join(list(zip(*text))[i][j:j+M])
                # 초보용
                # 기준위치(j,i) 에서부터 M만큼 더해가며 회문 완성
                result = ""
                for l in range(M):
                    result += text[j+l][i]

    print(f"#{tc} {result}")
