class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def arrayToLinkedList(array):
    head=None
    for i in range(len(array)):
        if(head):
            head.next=ListNode(array[i])
            head=head.next
        else:
            head=ListNode(array[i])
            toReturn=head

    return toReturn

def printLinkedList(listNode):

    while(listNode):
        print(listNode.val)
        listNode=listNode.next