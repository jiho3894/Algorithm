##################################
# 단지 번호 붙이기
# DFS


# BFS
from collections import deque

# 상,하,좌,우 방문
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph,a,b):
  n = len(graph) # 그래프 칸 수
  q = deque() # deque를 이용해 큐 구현
  q.append((a,b)) 
  graph[a][b] = 0 # 방문한 곳은 0 으로 표시
  c = 1 # 단지별 가구 수

  while q:
    x,y = q.popleft() # 해당 위치
    # 상,하,좌,우 이어져있는지 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 그래프 칸을 벗어난 위치 ( ex) [-1,0] [0,-1] )
      if nx < 0 or nx >= n or ny < 0 or ny >=n :
        continue # for문을 다시 돌림
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        q.append((nx,ny))
        print(q)
        c += 1
  return c

n = int(input()) # 지도의 크기 n*n
graph = [] # 지도에 들어가는 배열
for i in range(n):
  graph.append(list(map(int,input())))

cnt = [] #bfs 함수에서 return 시킨 c의 값을 담은곳 => 단지별 가구 수
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      cnt.append(bfs(graph,i,j))

print(cnt)
# 문제에서 가구 수를 정렬된 순서로 오름차순
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
  print(cnt[i])


