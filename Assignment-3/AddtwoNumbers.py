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


def addTwoLL(head1, head2):
    if head1 == None or head2 == None:
        return
    sum = 0
    carry = 0
    temp = None
    res = LinkedList()

    while head1 != None or head2 != None:
        first = 0
        second = 0
        if head1 != None:
            first = head1.data
        if head2 != None:
            second = head2.data
        sum = first + second + carry
        print(sum)
        res.push(sum % 10)
        carry = sum // 10
        if head1 != None:
            head1 = head1.next
        if head2 != None:
            head2 = head2.next

    if carry != 0:
        res.push(carry)
    return res




llist1 = LinkedList()
llist1.push(5)
llist1.push(6)
llist1.push(7)

llist2 = LinkedList()
llist2.push(5)
llist2.push(6)

#567 + 56

res = addTwoLL(llist1.head, llist2.head)
res.printList()




