numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for tc in range(1, T + 1):
    _, N = input().split()
    N = int(N)  # N 만 숫자로 바꾼다.

    text = input().split()  # split() 메서드의 return 타입은 배열(리스트)

    # 카운트 배열
    count = [0] * 10
    # count[0] : "ZRO" 문자열 등장횟수
    # count[1] : "ONE" 문자열 등장횟수....
    # count[9] : "NIN" 문자열 등장횟수

    for num in text:
        # text 안의 문자열 하나 가져와서 numbers 안에 있는 문자열이면 개수 증가
        for i in range(10):
            if num == numbers[i]:
                count[i] += 1

    answer = ""  # 빈 문자열 하나 만들어놓고 문자열 + 로 조합해서 테케 끝난후에 한번만 출력

    for i in range(10):
        answer = answer + (numbers[i] + " ") * count[i]

    # 출력을 마지막에 한번만
    print(f"#{tc} {answer}")
