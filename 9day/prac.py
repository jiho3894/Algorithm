###########################################
# 9회차 이진트리
# 비순환 구조로 부모와 자식관계가 정확함 부모의 자식은 최대 2개만 가질수있고 왼쪽부터 만들어짐

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###########################################
# 이진트리의 최대 깊이
# 이진트리의 최고점 1을 기준으로 내려가는 자식의 관계의 최대값을 구하는문제
# 1 - 1, 3 - 2, 4~7 - 3 이런식으로 트리의 구조에 들어가는값은 등기수열로 늘어남
from collections import deque  ## deque 사용 큐 형태


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: #ex) root:[1,null,2]
        if root is None: #이진 트리가 존재하지않으면 0으로 return 
            return 0
        q = deque([root]) # input값으로 들어가는것을 deque로 표현
        depth = 0 # 초기값

        while q: #q가 존재할때까지 while문
            depth += 1 # 반복 1회 실행시 마다 증가
            for _ in range(len(q)): # q의 길이만큼 for문 실행 ex) 3회
                cur = q.popleft() #가장 첫번째값은 1 고정이기때문에 빼고 왼쪽 오른쪽 하나씩 제거 [2]
                if cur.left: # 왼쪽부터 하나빼 ex) null이라 오른쪽임
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right) #q:[2]

        return depth
