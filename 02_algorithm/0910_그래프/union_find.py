N = 10
# N개의 원소가 있고, 집합을 만드려고 한다
p = [i for i in range(N)]
# p[i] => i가 가리키고 있는 사람 번호
# p[i] => i가 속한 집합의 대표(xxxxxxxxxxxxxxxx), 대표 일수는 있지만 100%는 아님

# 연산의 최적화를 위해서 트리의 높이를 관리하는 rank 배열
rank = [1] * N


# x 가 속한 집합의 대표를 찾는 연산
def find(x):
    # 집합의 대표가 되는 조건?
    # 부모를 가리키는 화살표가 자기 자신을 향할때 : 그친구가 대표
    if p[x] != x:
        # x가 자기 자신을 가리키고 있지 않으면 대표를 계속 찾아
        # 경로 압축(바로 대표를 가리키도록)
        p[x] = find(p[x])

    return p[x]


# x 가 속한 집합과 y 가 속한 집합을 합치는 연산
# 집합을 합친다 => 두 집합의 대표를 같게 한다.
def union(x, y):
    # x가 속한 집합의 대표
    rootX = find(x)
    # y가 속한 집합의 대표
    rootY = find(y)

    # 두 집합의 대표가 다를때만 합치자
    if rootX != rootY:
        # 두 집합의 높이를 비교해서 작은쪽을 큰쪽에 붙이자.
        if rank[rootX] > rank[rootY]:
            p[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            p[rootX] = rootY
        else:
            # 두 집합의 높이가 같을때는 한쪽에 다른쪽을 붙이고
            # 붙인 쪽 높이 + 1
            # y를 x에 붙인다고 치면
            p[rootY] = rootX
            # 높이가 증가해야 하는 쪽은 x
            rank[rootX] += 1
