# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#######################################
# 이진 트리의 직경
# 이진 트리에서 가장 길게 이어지는 길이를 구하는 문제 ex)이진트리 특성 무시 이미 지난곳은 돌아갈 수는없음
class Solution:
    def diameterOfBinaryTree(self, root: """ Optional[TreeNode] """) -> int:
        def get_length(node): # root값이 들어가 확인하는 함수 ex)[1,2,3,4,5]
            left_length = right_length = 0  #0으로 초기화
            if node.left: # 왼쪽 자식이 몇개인지
                left_length = get_length(node.left) + 1
            if node.right: # 오른쪽 자식이 몇개인지
                right_length = get_length(node.right) + 1
            res.append(left_length + right_length)
            
            return max(left_length,right_length)
            
        res = [0]
        if root:
            get_length(root)
            
        return max(res)