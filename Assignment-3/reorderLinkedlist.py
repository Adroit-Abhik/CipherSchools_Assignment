'''

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed

'''


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


def reverseIterative(head):
    if head == None:
        return
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head


def getMid(head):
    if head == None:
        return head
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def reOrder(head):
    if head == None or head.next == None:
        return
    # find middle element
    mid = getMid(head)
    midNext = mid.next
    # break it in to two parts
    mid.next = None

    left = head
    right = midNext

    # reverse the right part
    s = left
    t = reverseIterative(right)
    resHead = s

    # reordering
    while s or t:
        nexts = None
        nextt = None
        if s != None:
            nexts = s.next
            s.next = t
        if t != None:
            nextt = t.next
            t.next = nexts
        s = nexts
        t = nextt
    return resHead


llist = LinkedList()

llist.push(20)
llist.push(8)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

llist.printList()
print()

res = reOrder(llist.head)
llist.head = res

llist.printList()
