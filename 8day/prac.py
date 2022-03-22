n = int(input()) # 체스판 크기
visited = [-1] * n # 방문할 열
cnt = 0 # 결과값


def is_ok_on(nth_row):
    for row in range(nth_row):
        if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
            return False
    return True


def dfs(row):
    global cnt
    if row == n:
        cnt += 1
    else:
        for i in range(n):
            visited[row] = i
            if is_ok_on(row):
                dfs(row+1)
    return cnt


dfs(0) # 시작지점
print(cnt)
