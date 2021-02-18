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

def getCount(head):
    temp = head
    count = 0
    while temp != None:
        count += 1
        temp = temp.next
    return count

def getIntersectionNode(head1, head2):
    if head1 == None or head2 == None:
        return
    c1 = getCount(head1)
    c2 = getCount(head2)

    if c1 > c2:
        d = c1 - c2
        return getNode(head1, head2, d)
    else:
        d = c2 - c1
        return getNode(head2, head1, d)


def getNode(head1, head2, d):
    curr1 = head1
    curr2 = head2

    # reach curr1 to the same level as curr2
    for i in range(d):
        if curr1 == None:
            return -1
        curr1 = curr1.next
    # now increament them at the same time
    while curr1 and curr2:
        if curr1.data == curr2.data:
            return curr1.data
        curr1 = curr1.next
        curr2 = curr2.next
    return -1



ll1 = LinkedList()
ll1.push(10)
ll1.head.next = Node(12)
ll1.head.next.next = Node(15)
intersectionNode = ll1.head.next.next
ll1.head.next.next.next = Node(20)
ll1.head.next.next.next.next = Node(40)

ll2 = LinkedList()
ll2.push(5)
ll2.head.next = intersectionNode

ll1.printList()
print()
ll2.printList()
print()
print(getIntersectionNode(ll1.head, ll2.head))


