#########################
# 회차 강의 카드2 문제


from collections import deque #deque라는 python 모듈 스택에 앞배열 제거 같은 기능이 들어가 있음 ex) popleft O(n) -> O(1)
n = int(input()) # input
q = deque() # queue
for i in range(n): #input 수 만큼 배열에 숫자 순서대로 담기
    q.append(i+1)
while len(q) > 1: # q에 하나가 남을때 출력을 해야하기때문에 그 전까지 제거 작업
    q.popleft()
    q.append(q.popleft())
    
print(q[0])


###################################################
# 스택을 이용한 큐 구현
# 이 문제에서는 push,peek,pop,empty의 기능을 가져야하는 하나의 클래스를 생성해야함
# ex) push(n) -> q : [n]
# push(m) -> q: [n,m] -> 문제내 룰 가장 왼쪽이 큐의 맨 앞
# peek() -> q: [n,m] ? return n
# pop() -> q: [m]
# empty() -> q:[m] => q.length == 1 ? return False : return True

class MyQueue1:
    def __init__(self): # 큐를 구성한 list 생성
        self.input = []

    def push(self, x: int) -> None: 
        self.input.append(x) # input = [x]
        return self.input
    
    def pop(self) -> int: # 큐는 FIFO 구조이기때문에 가장 먼저간 값이 나가야함
        return self.input.pop(0)  

    def peek(self) -> int: # list의 가장 첫번째 값을 return
        return self.input[0]

    def empty(self) -> bool:
        return len(self.input) == 0

