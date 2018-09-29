from MyLibrary import ArrayLinkedListCollection

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        dummy=ListNode(1)
        p=dummy
        dummy.next=None

        while(head):
            if(head.val == val):
                head=head.next
                dummy.next=None
            else:
                dummy.next=head
                head=head.next
                dummy=dummy.next
        return p.next

a=ArrayLinkedListCollection.arrayToLinkedList([1,1, 1])

var=Solution()
p=var.removeElements(a, 2)

ArrayLinkedListCollection.printLinkedList(p)