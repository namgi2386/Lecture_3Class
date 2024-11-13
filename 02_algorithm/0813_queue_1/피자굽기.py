T = int(input())

for tc in range(1, T + 1):
    # N : 오븐에 들어갈 수 있는 피자 개수
    # M : 우리가 구워야하는 총 피자 개수
    N, M = map(int, input().split())

    # 각 피자의 치즈 양 리스트
    pizza = list(map(int, input().split()))

    # 원형 큐 == 오븐
    qsize = N + 1  # 원형 큐의 크기, 빈칸이 하나 필요(front)
    oven = [0] * qsize
    front = rear = 0

    # 맨 처음에는 N(오븐의 크기)개 피자를 꺼내서 오븐에 넣기
    for i in range(N):
        rear = (rear + 1) % qsize
        oven[rear] = i  # 피자 번호 i (0번부터, 문제에서는 1번부터)

    # 오븐에 자리가 남으면 다음에 들어갈 피자의 번호
    next_pizza = N

    # 꺼낸 피자 번호(인덱스)
    pizza_num = 0

    # 오븐에서 계속 피자를 꺼냈다가 넣었다가
    # 오븐안에 피자가 남았으면 계속해
    while front != rear:
        # 오븐안에서 피자 하나 꺼내기
        front = (front + 1) % qsize
        pizza_num = oven[front]

        # 치즈를 반으로 녹이자
        pizza[pizza_num] = pizza[pizza_num] // 2

        # 반으로 녹였는데 아직 치즈가 남았으면 오븐에 다시 넣고
        if pizza[pizza_num] > 0:
            rear = (rear + 1) % qsize
            oven[rear] = pizza_num  # 피자 번호

        # 치즈가 0이 됬으면 꺼내고 새로운 피자를 넣자
        else:
            # 아직 구울수 있는 피자가 남아있거나
            # 다음에 넣을 피자 번호가 아직 인덱스 범위 안
            if next_pizza < M:
                rear = (rear + 1) % qsize
                oven[rear] = next_pizza  # 피자 번호
                next_pizza += 1  # 다음에 넣을 피자 번호 + 1

            # 현재 이 피자가 마지막 피자 이거나
            # 마지막 피자면 오븐이 비었기 때문에 반복문 자동 종료
    
    # 마지막으로 꺼낸 피자 번호 + 1 해서 출력
    print(f"#{tc} {pizza_num + 1}")
