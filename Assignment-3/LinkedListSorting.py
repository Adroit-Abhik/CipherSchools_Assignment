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

def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    res = Node(-1)
    curr = res

    while head1 != None or head2 != None:
        if head1 == None:
            curr.next = head2
            curr = head2
            head2 = head2.next
        elif head2 == None:
            curr.next = head1
            curr = head1
            head1 = head1.next
        elif head1.data < head2.data:
            curr.next = head1
            curr = head1
            head1 = head1.next
        else:
            curr.next = head2
            curr = head2
            head2 = head2.next

    return res.next


def getMid(head):
    if head == None:
        return head
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def mergeSort(head):
    if head == None or head.next == None:
        return head
    mid = getMid(head)
    midNext  = mid.next

    mid.next = None
    left = mergeSort(head)
    right = mergeSort(midNext)

    sortedHead = merge(left, right)
    return sortedHead


ll1 = LinkedList()
ll1.push(15)
ll1.push(2)
ll1.push(20)
ll1.push(6)

ll1.printList()
print()
newHead = mergeSort(ll1.head)
ll1.head = newHead
ll1.printList()




