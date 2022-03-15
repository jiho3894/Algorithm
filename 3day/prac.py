##############################################
# 3회차 스택
# push pop
# push : 하나의 리스트에 데이터를 넣는다 넣고 쌓아가는 구조
# pop : 만들어진 데이터에 가장 뒤에 쌓인것을 빼는
# LIFO: Last in first out 구조 

# 노드 생성
class Node:
    def __init__(self, item, next) -> None:
        self.item = item # 들어갈 아이템
        self.next = next # 아이템의 쌓는 순서

    class Stack:
        def __init__(self) -> None:
            self.top = None

        def push(self, value): 
            self.top = Node(value, self.top)

        def pop(self):
            # top이 없다는 조건을 넣어줘야 처음 self.top.next때 오류가 안남
            if self.top is None:
                return None

            node = self.top
            self.top = self.top.next

            return node.item

        def is_empty(self):
            return self.top is None

################################
# 회차별 문제
# 유효한 괄호
# assert는 다음의 값이 무조건 True 이여야만함
# assert test_problem_stack("()") = true
# assert test_problem_stack("()[]{}") = true
# assert not test_problem_stack("(]") = false
# test_problem_stack(s : str)

class Solution:
    def isValid(self, s: str) -> bool:
        # 여기서 : 는 정확히 뭘 의미하는건지 ( ket value 값 )
        pair = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        opener = "{(["
        stack = []
        
        for char in s:
            if char in opener:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pair[char] != top:
                    return False
        return not stack