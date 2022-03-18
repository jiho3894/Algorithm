n = int(input())  # 컴퓨터의 수
m = int(input())  # 현재 존재하는 쌍
graph = [[]*n for _ in range(n+1)]  # 컴퓨터의 수 만큼 배열 생성 [[],[]...]
for _ in range(m): # 존재하는 쌍만큼 들어가는 배열 값 생성
    a, b = map(int,input().split())  # 쌍 별로 연결리스트 구성 #쌍 별로 연결리스트 구성
    graph[a].append(b)
    graph[b].append(a)
print(graph)
print(graph[1]) 

cnt = 0
visited = [0] * (n+1)
print(visited)

def dfs(v):
    global cnt
    visited[v] = 1 # visited[1] = 1
    for i in graph[v]: #2 , 5 입력값 반복 
        if visited[i] == 0: # true
            print(f'{i}')
            print(visited)
            dfs(i) # 1
            cnt += 1

dfs(1)
print(cnt)
