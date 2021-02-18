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

    def reverseK(self, k):
        curr = self.head
        prev_first = None
        is_first_pos = True

        while curr:
            first = curr
            prev = None
            count = 0
            while curr and count < k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                count += 1
            if is_first_pos:
                self.head = prev
                is_first_pos = False

            if prev_first != None:
                prev_first.next = prev
            prev_first = first



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
llist.reverseK(3)
llist.printList()

