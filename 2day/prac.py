################################
# 2회차 연결 리스트
# Array vs Linked List
# Array : index를 통해 직접적으로 접근할 경우 시간 복잡도 O(1)
# 중간에 삽입 또는 삭제를 할때는 뒤에서 하나씩 빼줘야함 시간 복잡도 O(n)
# ex) remove는 1번째 index , pop은 마지막 index
# q1) 이 과정이 O(n)의 일부분?
arr1 = [1, 2]
print(arr1[0])  # Array 접근
arr2 = [1, 2, 3]
arr2.insert(1, 4)  # 중간에 값 추가
print(arr2)  # [1,4,2,3]
del arr2[2]
print(arr2)  # [1,4,3]

## 연결리스트는 선형 자료구조 ( 하나의 자료 뒤에 하나의 자료가 존재하는 1대1관계)
# 비선형 자료구조는? 하나 자료뒤에 여러개의 자료가 존재할수있음 (1대1 or 1대n)
# Linked List : 연결 리스트는 직접 구현하며
# 접근이 어려움 시간 복잡도 O(n)
# 중간에 삽입 또는 삭제를 할때는 중간에 값을 바로 찾을 수 있음 시간 복잡도 O(1)
# 연결 리스트 구현 코드

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        if not self.head:
            self.head = ListNode(val, None)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)



lst = [1, 2, 3, 4, 5]
li = LinkedList()
for e in lst:
    li.append(e)
print(li)


#####################################
# 팰른드롬 연결 리스트 ( 앞 뒤가 똑같은 )

def isPalindrome(head):
    arr = []

    if not head:
        return True

    node = head
    while node:
        arr.append(node.val)
        node = node.next

    while len(arr) > 1:
        if arr.pop(0) != arr.pop():
            return False

    return True
