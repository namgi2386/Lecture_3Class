lst = [1, 2, 3, 4, 5]

N = 5


# idx : 현재 순열의 i번째 자리에 올 원소를 선택하고 있다.
# selected : 순열을 만들때 이전에 사용했던 원소 체크(중복 선택 방지)
# result : 지금까지 만든 순열
# n : 순열 길이
def make_perm(idx, selected, result, n):
    # 종료 조건
    if idx == n:
        # 지금까지 만든 순열 출력
        print(result)
        return

    # 재귀 호출
    # 현재 순열의 idx 번째 자리에 놓을 원소를 선택
    # 이전에 고른적이 없는 원소를 자리에 놓아야 한다.
    # 내가 고를수 있는 원소는 lst안에 있음, lst 인덱스 범위 : 0 ~ n-1
    for i in range(n):
        # i번 원소를 이전에 고른적이 없다 => 순열의 idx번째 자리에 i번 원소를 놓는다.
        if not selected[i]:
            # i번째 원소 골랐다고 체크
            selected[i] = 1
            result.append(lst[i])
            # idx+1 번째 자리 원소 정하러 가기
            make_perm(idx + 1, selected, result, n)

            # i번째 원소를 원상복귀
            # idx번째 자리에 i+1,i+2,,,, 번재 원소를 골라야 할수도 있으니까.
            selected[i] = 0
            result.pop()


make_perm(0, [0] * N, [], N)
