T = int(input())

for tc in range(1, T + 1):
    N, X = map(int, input().split())

    land = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for i in range(N):
        # 가로
        row_check = [0] * N
        for j in range(1, N):
            prev = land[i][j - 1]  # 가로니까 (i,j-1) 높이
            now = land[i][j]  # (i,j) 높이
            make = True
            if now > prev:  # 지금 높이가 이전보다 크면
                for k in range(1, X + 1):  # 왼쪽으로 이동하면서 길이 X만큼의 활주로를 만들수 있는지 검사, 모든 위치의 높이 + 1 은 now와 같아야함(경사로의 높이는 모두 1)
                    if j - k >= 0 and row_check[j - k] != 1 and land[i][j - k] + 1 == now:
                        row_check[j - k] = 1
                        continue
                    else:
                        make = False
                        break

            if now < prev:  # 지금 높이가 이전보다 작으면
                for k in range(X):  # 오른쪽으로 이동하면서 길이 X만큼의 활주로를 만들수 있는지 검사, 모든 위치의 높이 + 1 은 prev와 같아야함(경사로의 높이는 모두 1)
                    if j + k < N and row_check[j + k] != 1 and land[i][j + k] + 1 == prev:
                        row_check[j + k] = 1
                        continue
                    else:
                        make = False
                        break

            # 이번 행에서 만들지 못하면 검사 중단, 다음 행으로
            if not make:
                break

            # 중간에 경사로 조건대로 다 놓았고, 마지막 열까지 왔으면 이 행은 활주로 건설 가능
            if j == N - 1:
                # print(land[i])
                answer += 1

        # 세로
        col_check = [0] * N
        for j in range(1, N):
            prev = land[j - 1][i]
            now = land[j][i]
            make = True
            if now > prev:
                for k in range(1, X + 1):
                    if j - k >= 0 and col_check[j - k] != 1 and land[j - k][i] + 1 == now:
                        col_check[j - k] = 1
                        continue
                    else:
                        make = False
                        break

            if now < prev:
                for k in range(X):
                    if j + k < N and col_check[j + k] != 1 and land[j + k][i] + 1 == prev:
                        col_check[j + k] = 1
                        continue
                    else:
                        make = False
                        break

            if not make:
                break

            if j == N - 1:
                # for k in range(n):
                #     print(f"{land[k][i]}")
                # print("--")
                answer += 1

    print(f"#{tc} {answer}")

# 1
# 8 3
# 2 2 2 3 3 4 2 2
# 2 2 2 3 3 4 2 2
# 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2
# 2 2 2 2 1 1 2 2
# 2 1 1 1 1 1 1 1
# 2 1 1 1 1 1 1 1
# 2 1 1 1 1 1 1 1

# 1
# 6 2
# 3 3 3 2 1 1
# 3 3 3 2 2 1
# 3 3 3 3 3 2
# 2 2 3 2 2 2
# 2 2 3 2 2 2
# 2 2 2 2 2 2
