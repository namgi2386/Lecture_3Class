A = [1, 2, 3, 4, 5]

N = 5


# idx : 부분집합에 넣을지 말지 결정하는 원소의 위치
# selected : 다음 재귀호출에서 이전 단계에서 골랐던 원소들을 알려줄 배열
def subset(idx, selected):
    # 1. 종료 조건(인덱스 범위)
    if idx == N:
        print(selected)
        return

    # 2. 재귀 호출
    # 각 단계에서 분기 수만큼 재귀 호출
    # 부분집합에서 분기는 idx 번째 원소를 선택 or 선택하지 않거나 2가지

    # idx번째 원소를 골랐다. => 선택하고 idx+1 번째 원소를 선택하러 가기
    subset(idx + 1, selected + [A[idx]])
    # 분기가 나뉘어 질때는 이전 선택에서 했던 일을 원래대로 되돌리는 과정 필요 할수도..

    # idx번째 원소를 고르지 않고 idx + 1번째 원소를 선택하러 가기
    subset(idx + 1, selected)


subset(0, [])
