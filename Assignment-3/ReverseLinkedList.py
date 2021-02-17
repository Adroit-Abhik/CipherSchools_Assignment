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

    def reverseIterative(self):
        if self.head == None:
            return
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def reverRecHelp(self, curr, prev):
        # if its the last node
        if curr.next == None:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev

        self.reverRecHelp(next, curr)

    def reverseRecursive(self):
        if self.head == None:
            return
        self.reverRecHelp(self.head, None)


llist = LinkedList()
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

llist.printList()
print()
llist.reverseIterative()
llist.printList()
print()
llist.reverseRecursive()
llist.printList()

