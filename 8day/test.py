n = int(input()) # 체스판의 크기 n*n
visited = [-1] * n # 방문한 곳 체크
cnt = 0 # 경우의 계산


def is_ok_on(nth_row):  # 방문시 주변 노드 탐색 백트래킹 퀸의 조건에 맞게
    for row in range(nth_row):
        if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
            return False
    return True


def dfs(row):  # 조건에 맞을시 경우의수에 포함
    if row >= n:
        global cnt
        cnt += 1
        return cnt
    for col in range(n):
        visited[row] = col
        if is_ok_on(row):
            dfs(row + 1)


dfs(0)
print(cnt)
