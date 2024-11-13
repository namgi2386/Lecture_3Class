N = 5
arr = [[N*j + i for i in range(1, N+1)] for j in range(N)]


def recul(i, j, N):
    if i > N-1:
        return
    elif j > N-1:
        print()
        return recul(i+1, 0, N)
    else:
        print(arr[i][j], end=" ")

    recul(i, j+1, N)
recul(0, 0, N)