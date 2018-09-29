from MyLibrary import ArrayLinkedListCollection

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        shortHead=ListNode(2)
        largeHead=ListNode(2)
        shortHead_2=shortHead
        largeHead_2=largeHead

        while(head):
            if(head.val>=x):
                largeHead.next=head
                largeHead=head
                head=head.next
            else:
                shortHead.next=head
                shortHead=head
                head=head.next
        largeHead.next=None
        shortHead.next=largeHead_2.next
        return shortHead_2.next
array=[1,4,3,2,5,2]
p=ArrayLinkedListCollection.arrayToLinkedList(array)

var=Solution()
x=var.partition(p, 3)

ArrayLinkedListCollection.printLinkedList(x)




