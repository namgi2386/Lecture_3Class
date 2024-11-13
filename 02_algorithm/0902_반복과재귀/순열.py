A = [1, 2, 3, 4]
N = 4




# idx : 현재 자리 번호
# used : 내가 이전까지 골랐던 숫자 번호 리스트
# path : 현재까지 완성한 순열
def perm(idx, path, used):
    # 종료 조건
    if idx == N:
        print(path)
        return


    # 아직 정할 자리가 남았다면
    # 내가 선택할수 있는 번호 골라서 idx번째에 놓기
    for i in range(N):
        # i번을 내가 이전에 선택한적이 없다면 idx 자리에 놓기
        if i not in used:
            # 현재 순열에 A[i] 추가, i번째 숫자를 중복선택하지 않도록 체크
            perm(idx + 1, path + [A[i]], used + [i])




# perm(0, [], [])




# 고정된 크기의 배열과 인덱스 사용
# path = [0,0,0]
# used = [F,F,F]
def perm2(idx, path, used, N, R):

    # N 개 중에 R개 골라서 순열
    if idx == R:
        print(path)
        return


    for i in range(N):
        # 이전에 내가 i번 숫자 놓은적 없으면
        if used[i] == False:
            # idx 자리에 i번 숫자 놓아보기
            path[idx] = A[i]
            # i번 숫자는 골랐으니까 idx + 1 부터는 사용하면 안된다.
            used[i] = True
            # idx + 1 자리 선택하러 가기
            perm2(idx + 1, path, used, N, R)
            # 끝나고 돌아오면 i번 숫자는 다시 선택 안한것으로 바꾸기 => idx에 i번 말고 다른 숫자(i+1,i+2..)도 놓아봐야 하니까
            used[i] = False
            # path[idx]는 어차피 다음에 내가 고르지 않은 숫자로 바뀌게됨


# 3개만 골라서
R = 3
path = [0] * N
used = [False] * N
perm2(0, path, used, N, R)
