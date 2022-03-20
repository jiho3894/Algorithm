############################################
# 2일차 과제 - 두 정렬 리스트의 병합 ( 정렬되어 있는 두 연결 리스트를 합쳐라 )
# 두개의 정렬된 리스트를 입력받고 두 리스트를 이용하여 하나의 정렬된 리스트를 반환하는 문제
# 정렬된 값을 만들어야 하기때문에 각 배열의 순서별로 크기를 체크하고 조건에 맞을시
# 하나의 리스트로 구성된 리스트에 집어넣어야함

# 연결 리스트 생성
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

### l1 = [1,2,4] , l2 = []
class LinkedList:
    def mergeTwoLists(self, l1 : ListNode, l2 : ListNode) -> ListNode :    #l1 , l2
        node = ListNode(0, None)  # 노드 박스 하나 생성 값 초기화
        cur = node # 박스를 current에 넣어놓기
        while l1 and l2:  # l1과 l2 둘다 배열이 존재할경우
            if l1.val <= l2.val: #l1의 노드 val 값이 l2보다 작거나 같으면
                cur.next = l1 # current의 첫 박스의 노드 값은 l1
                l1 = l1.next # l1의 next 생성
            else:  
                cur.next = l2 # l1이 더 크다면 current에 l2를 넣어주기
                l2 = l2.next # 그 다음 값에 next 생성
            cur = cur.next # l1 l2 배열 값을 모두 while 횟수만큼 뽑아내고 next를 하나 더 생성
        cur.next = l1 or l2 # 그리고 그 다음값중에 l1 l2에 남아 있는 값을 밀어 넣어주기
        return node.next 

li1 = [1, 2, 3]
li2 = [2, 3, 4]
li = LinkedList()
for e in li:
    li.mergeTwoLists(e)
print(li)
