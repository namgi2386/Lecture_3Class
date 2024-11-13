# 우선 순위 표
# () > */ > +-

# 스택 밖에 있을때 우선순위
icp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 3}
# 스택 안에 있을때 우선순위
isp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}


# 중위표기식(infix) => 후위표기식(postfix)
# infix : 후위표기식으로 바꿀 중위표기식
# n : 식의 길이
def get_postfix(infix, n):
    # 결과로 출력할 후위표기식
    postfix = ""

    stack = []

    # 문자열에서 하나씩 떼어와서 식 만들자
    for i in range(n):
        # infix[i] => 중위표기식의 i번째 글자
        if infix[i] not in "(+-*/)":
            # i번째 글자가 피연산자다. => 결과에 출력
            postfix += infix[i]
        else:
            # i번째 글자가 닫는 괄호인가?
            if infix[i] == ")":
                # 여는 괄호가 나올때까지 pop 해서 결과에 출력
                while stack:
                    # 연산자 하나 꺼내기
                    op = stack.pop()
                    # 꺼냈는데 여는 괄호면 꺼내기 중단
                    if op == "(":
                        break

                    # 여는 괄호가 아니었다 => 출력
                    # 괄호 안에 있는 연산자는 최우선 으로 계산되어야한다.
                    postfix += op

            # i번째 글자가 연산자다 => 우선순위 보고 판별
            else:
                # 현재 연산자(infix[i])의 우선순위보다 => icp[infix[i]]
                # 스택의 top 에 있는 연산자(stack[-1])의 우선순위(isp[stack[-1]])가 같거나 높으면
                # pop 해서 출력한다 => 우선순위가 높은 연산자를 먼저 계산해야 하기 때문
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()

                # 스택의 탑에 있는 연산자의 우선순위가 나보다 작으면
                # 나보다 우선순위가 같거나 높은친구들은 위에서 다 뽑아버렸기 때문에 그냥 push
                stack.append(infix[i])

    # 스택에 남은 연산자 모두 출력
    while stack:
        postfix += stack.pop()

    return postfix


infix = "(6+5*(2-8)/2)"
postfix = get_postfix(infix, len(infix))

print(postfix)


# 후위표기식을 계산 함수
def get_result(postfix):
    stack = []

    # 후위표기식에서 글자 하나씩 떼어오기
    for token in postfix:

        # 떼어온 토큰이 피연산자면 스택에 넣기
        if token not in "+-*/":
            stack.append(int(token))  # 타입 조심

        # 토큰이 연산자인 경우 연산에 필요한 만큼 스택에서
        # 피연산자를 꺼낸 후에 연산
        # 이 연산 결과를 다음 연산자가 또 써야 하기 때문에 다시 push
        else:
            # 오른쪽 피연산자가 먼저 나온다.
            right = stack.pop()
            # 왼쪽이 나중에
            left = stack.pop()

            # 계산 결과
            result = 0

            # 연산자의 종류에 따라서 계산
            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                result = left / right

            # 계산 결과를 다음 연산자가 써야하니까 스택에 다시 push
            stack.append(result)

    # 계산이 잘 됬다면 스택 안에는 결과가 하나 남아있을 것이다.
    return stack.pop()


result = get_result(postfix)

print(result)
