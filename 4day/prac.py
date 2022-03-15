#################################
# 4회차 큐
# FIFO : first in first out

# 노드 생성
class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = next


class Queue:
    def __init__(self) -> None:
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value, None)
            return

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(value, None)

    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next
        return node.item

    def is_empty(self):
        return self.front is None


lst = [1, 2]
li = Queue()
for e in lst:
    li.pop()
print(li)
