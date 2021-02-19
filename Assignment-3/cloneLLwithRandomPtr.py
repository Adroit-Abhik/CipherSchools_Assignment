class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


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
            print('Data = ', temp.data, ' Random = ', temp.random.data)
            temp = temp.next


def clone(head):
    if head == None:
        return
    temp = head
    # creating duplicates
    while temp:
        next = temp.next
        dup = Node(temp.data)
        temp.next = dup
        dup.next = next
        temp = temp.next.next
    # copying random pointer of original to dups
    curr = head
    while curr:
        curr.next.random = curr.random.next
        curr = curr.next.next
    # breaking links
    curr = head
    dup_head = head.next
    while curr.next:
        next = curr.next
        curr.next = curr.next.next
        curr = next
    return dup_head


org = LinkedList()
org.head = Node(1)
org.head.next = Node(2)
org.head.next.next = Node(3)
org.head.next.next.next = Node(4)
org.head.next.next.next.next = Node(5)

original_list = org.head

original_list.random = original_list.next.next

# 2's random points to 1
original_list.next.random = original_list

# 3's random points to 5
original_list.next.next.random = original_list.next.next.next.next

# 4's random points to 5
original_list.next.next.next.random = original_list.next.next.next.next

# 5's random points to 2
original_list.next.next.next.next.random = original_list.next

print('Original List: ')
org.printList()

dup = LinkedList()
dup.head = clone(original_list)

print('\nCloned List: ')
dup.printList()


