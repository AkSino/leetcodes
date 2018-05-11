class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.val

class Solution:
    def swapPairs(self, head):
        if not head:
            return None
        first=ListNode(1)
        pick=first
        if head.next:
            first.next = head.next
        else:
            return head
        while head and head.next :
            pick.next=head.next
            backup=head.next.next
            head.next.next=head
            head.next=backup
            pick=head
            head=backup
        return first.next

a=ListNode(1)
a.next=ListNode(2)
a.next.next=ListNode(3)
a.next.next.next=ListNode(4)

var=Solution()
b=var.swapPairs(a)
while b:
    print(b.val)
    b=b.next
