class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def printList(self):
        current = self.head
        while current:
            print(current.data, end = ' -> ')
            current = current.next
        print('None')

    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        prev = self.head
        for _ in range(index -1):
            prev = prev.next

        # 새 Node의 Next는 Prev Node의 Next
        new_node.next = prev.next
        # Prev Node의 Next는 새 Node
        prev.next = new_node

    def delete(self, index):
        # List가 비어있는지 확인
        if self.head is None:
            raise IndexError("List is Empty")
        
        # 헤드를 삭제할 경우
        if index == 0:
            self.head = self.head.next
            return
        
        # 해당 index가 정상적인지 확인
        prev = self.head
        for _ in range(index - 1):
            if prev.next is None:
                raise IndexError("Index out of range")
            
        if prev.next is None:
            raise IndexError("Index out of range")
        
        prev.next = prev.next.next

    def get(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        if current is None:
            raise IndexError("Index out of range")
        
        return current.data
    
    def update(self, index, item):
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        if current is None:
            raise IndexError("Index out of range")
        
        current.data = item
