class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def detectLoop(self):
        slow = fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                self.removeLoop(slow, fast)
                return True
        return False

    def removeLoop(self, slow, fast):
        if slow == fast:
            slow = self.head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

            fast.next = None


llist = LinkedList()
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

llist.head.next.next.next.next = llist.head.next

print(llist.detectLoop())
print(llist.detectLoop())

llist.printList()

