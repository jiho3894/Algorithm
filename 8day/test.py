n = int(input())
visited = [-1] * n
cnt = 0


def is_ok_on(nth_row):
    for row in range(nth_row):
        if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
            return False
    return True


def dfs(row):
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
