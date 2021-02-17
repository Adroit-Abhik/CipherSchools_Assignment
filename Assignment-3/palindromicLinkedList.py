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

    # with extra space
    def checkPalindrome(self):
        if self.head == None:
            return

        stack = []
        curr = self.head

        while curr != None:
            stack.append(curr.data)
            curr = curr.next
        temp =self.head
        while temp != None:
            el = stack.pop(-1)
            if temp.data != el:
                return False
            temp = temp.next
        return True




llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(2)
llist.push(1)


llist.printList()
print(llist.checkPalindrome())


