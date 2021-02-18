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

    def removeAllOccurances(self):
        if self.head == None or self.head.next == None:
            return
        temp = Node(-1)
        temp.next = self.head
        res = temp

        prev = temp
        curr = self.head

        while curr and curr.next:
            val = curr.data
            while curr.next and curr.next.data == val:
                curr = curr.next
            if curr != prev.next:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        self.head = res.next


ll = LinkedList()
ll.push(53)
ll.push(53)
ll.push(35)
ll.push(28)
ll.push(28)
ll.push(28)
ll.push(23)

ll.printList()
print()
ll.removeAllOccurances()
ll.printList()






