# BFS, DFS

# DFS
# 위상정렬은 하나의 선형 순서가 결과로 나온다.
# 간선의 방향성을 유지하면서 그래프의 모든 정점을 나열
# N개의 정점
# [v1, v2, v3, v4, v5... vN]
# 어떤 간선을 (vi, vj)이렇게 나타 냈을때 i < j

# 비순환 그래프 에서만 가능
# 결과가 유일하지 않을 수 있다.

# 깊이 우선 탐색 기반의 위상정렬
# DFS(깊이 우선 탐색)을 수행하면서 각 노드가 처리 되는 순서를
# 스택에 저장

# 모든 노드를 방문한 다음에 스택의 내용을 역순으로 정렬하면 결과 도출

# 1. 방문하지 않은 모든 정점에 대해서 DFS 실행
# 2. 어떤 정점에 대해서 그 정점과 인접한 모든 정점을 방문한 후에 스택에 추가
# => 현재 정점에서 갈 수 있는 모든 정점을 다 탐색 하고 난 뒤에 현재 정점을 스택에 추가
# 3. 스택을 역순으로 정렬하면 위상정렬이 된다.

# 그래프
G = [[] for _ in range(5)]
# 방문한 정점을 체크하기 위한 집합(중복체크)
visited = set()
# 정점을 담을 스택
stack = []

# 정점을 방문하는 재귀 함수
def dfs(node):
    # 노드 방문 처리
    visited.add(node)

    # 이 노드와 연결되어 있는 노드들을 모두 탐색
    for next_node in G[node]:
        # 이 연결되어 있는 노드를 방문한 적이 없으면 방문
        if next_node not in visited:
            dfs(next_node)

    # 이 노드에서 탐색 가능한 모든 노드 처리가 끝나면
    # 그때 스택에 추가
    stack.append(node)


print(stack[::-1])