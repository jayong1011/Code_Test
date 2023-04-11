from collections import deque
N , M, V = map(int, input().split())

graph  = [[] for _ in range (N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
print(graph)

def dfs(graph, v, visted):
    visted[v] = True
    print(v, end =" ")
    for i in graph[v]:
        if not visted[i]:
            dfs(graph, i, visted)



# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        # print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for k in graph[v]:
            if not visited[k]:
                queue.append(k)
                visited[k] = True
                
                
visted = [False] * (N+1)
visted1 = [False] * (N+1)
dfs(graph, V, visted)
print("")
bfs(graph, V, visted1)