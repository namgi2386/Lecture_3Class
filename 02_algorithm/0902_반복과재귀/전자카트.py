T = int(input())


# 단계는 v의 길이를 통해서 구별할 수 있다.
# now : 현재 내가 방문한 구역 번호
# v : 지금까지 순열을 만드는데 사용했던 인덱스 번호(중복체크)
# e_sum : now 자리까지 정했을때 에너지 사용량 합
def perm(now, e_sum, v):
    global min_energy

    # 가지치기
    # 현재까지 구한 에너지의 합이 내가 알고있는 최소값보다 크면
    # 이이상 진행할 필요가 있나?? 다음위치로 가는것을 중단\
    if e_sum >= min_energy:
        return


    # 종료 조건
    # 모든 방을 다 방문했으면 종료
    if len(v) == N:
        # v에 내가 방문한 구역번호를 추가 할건데,
        # v의 길이가 N이면 모든 구역을 방문 했다.
        # 시작지점으로 돌아가는 에너지 사용량도 고려해서 최소값 구하기
        min_energy = min(min_energy, e_sum + energy[now][0])
        return

    # 재귀 호출
    # 다음에 갈 수 있는 구역의 번호를 탐색
    # 0부터 N-1 까지
    # 갈 수 있는 구역의 번호? 내가 이전에 간적이 없는 번호면 갈 수 있다.
    for next in range(N):
        # next번 구역을 내가 이전에 간적이 없어야 한다.
        if next not in v:
            # next번 구역을 이번 차례에 갔다고 처리하고 다음 차례 방을 고르러 출발
            perm(next, e_sum + energy[now][next], v + [next])


for tc in range(1, T + 1):
    N = int(input())  # 구역의 개수

    # 각 구역으로 이동할 때마다 사용하는 배터리 양
    # energy[i][j] => i번 방에서 j번 방으로 이동하는데 사용하는 배터리 양
    # energy[i][j] != energy[j][i]
    energy = [list(map(int, input().split())) for _ in range(N)]

    # 내가 지금까지 순열을 만드는데 사용했던 번호 중복체크
    # 0번 구역, 그러니까 사무실은 제외하고 방문
    v = [0]

    # 최소 배터리 사용량
    min_energy = 10000
