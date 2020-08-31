class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head =  None
        self.size = 0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cur = self.head
        
        if index >= self.size or index <0:
            return -1
        
        if index == 0:
            print(self.head.val)
            return self.head.val
        
        for _ in range(0, index):
            cur = cur.next
        
        return cur.val
        
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        self.size += 1
        
        
        return

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head
        
        while curr.next is not None:
            curr = curr.next
            
        curr.next = Node(val)
        
        self.size += 1
        
        return
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
            
        curr = self.head
        
        for i in range(0,index-1):
            curr = curr.next
        
        temp = Node(val)
        temp.next = curr.next
        curr.next = temp
        
        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.size-1:
            return 
        
        if index == 0:
            self.head = self.head.next
            return
        
        curr = self.head
        
        for _ in range(index-1):
            curr = curr.next

        if curr.next.next is not None:
            curr.next = curr.next.next
        else:
            curr.next = None
        
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)