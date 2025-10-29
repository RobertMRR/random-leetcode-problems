class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def traverseList(node):
    currentNode = node
    while currentNode:
        print(f"current node: {currentNode.val}")
        currentNode = currentNode.next

head = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
head.next = node2
node2.next = node3
node3.next = node4

traverseList(head)
def reverseList(node):
    currentNode = node
    while currentNode:
        tmp = currentNode.next
        tmp2 = currentNode.val
        currentNode.val = tmp
        currentNode.next = tmp2
        currentNode = tmp
