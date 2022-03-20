######################################
# 6회차 . DFS (Depth-First Search) 깊이 우선 탐색
# 하나의 정점으로부터 차례대로 모든 정점들을 한번씩 방문함
# 최대한 깊게 내려가고 더 이상 내려갈 수 없을때 옆으로 넘어감

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

## 재귀함수
def dfs_recursive(node, visited):
    # 방문처리
    visited.append(node)

    # 인접 노드 방문
    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(adj, visited)

    return visited

## 스택
def dfs_stack(start):
    visited = []
    # 방문할 순서를 담아두는 용도
    stack = [start]

    # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
    while stack:
        # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
        top = stack.pop()
        visited.append(top)
        # 인접 노드를 방문한다.
        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return visited

########################
# 섬의 개수
# "0","1"로 이루어진 배열에서 "1"로 이어져있는 하나의 섬이 존재하는데 그 섬의 개수를 찾는 문제
# "1"의 4방향을 검사해 숫자를 확인해 섬의 크기를 측정

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

def island_dfs_stack(grid):
    # 상, 하 , 좌 , 우
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 열과 행 열rows:4 행cols:5
    rows, cols = len(grid), len(grid[0])
    cnt = 0 #섬의개수

    # grid의 모든 값 탐색 O(n*n)
    for row in range(rows):
        for col in range(cols):
          # [0,0] 1과 같지않다면 continue 다시 반복문을 돌린다는뜻
            if grid[row][col] != '1':
                continue
            # cnt = 9
            cnt += 1
            # statck [(0,0)]
            stack = [(row, col)]
            # 스택이 존재할때까지 while문 실행
            while stack:
                # x = 0 , y = 0
                x, y = stack.pop()
                # 1이 확인된 자리를 0으로 변경
                grid[x][y] = '0'
                # 상하좌우를 확인하기 위해 4번 확인
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    stack.append((nx, ny))
    return cnt


assert island_dfs_stack(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_stack(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3