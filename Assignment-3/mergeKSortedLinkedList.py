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



def mergeKlists(lists, start, end):
    if start == end:
        return lists[start]
    mid = start + (end - start) // 2
    left = mergeKlists(lists, start, mid)
    right = mergeKlists(lists, mid+1, end)

    return merge(left, right)

def mergeList(lists, k, n):
    if lists == None or k == 0:
        return None
    return mergeKlists(lists, 0, k-1)





k = 3
n = 4
ll1 = LinkedList()
ll1.push(7)
ll1.push(5)
ll1.push(3)
ll1.push(1)

ll2 = LinkedList()
ll2.push(8)
ll2.push(6)
ll2.push(4)
ll2.push(2)

ll3 = LinkedList()
ll3.push(11)
ll3.push(10)
ll3.push(9)
ll3.push(0)


resultHead = mergeList([ll1.head, ll2.head, ll3.head], 3, 4)
resL = LinkedList()
resL.head = resultHead

resL.printList()
