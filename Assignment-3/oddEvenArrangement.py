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

    def evenOddArrangement(self):

        if self.head == None or self.head.next == None:
            return

        odd = self.head
        self.head = odd
        even = self.head.next
        evenhead = even

        while even.next != None and odd.next != None:
            odd.next = even.next
            if even.next != None:
                odd = even.next

            even.next = odd.next
            if odd.next != None:
                even = odd.next
        odd.next = evenhead

ll = LinkedList()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)

ll.printList()
print()
ll.evenOddArrangement()
ll.printList()


