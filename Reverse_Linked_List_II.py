class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):

        if(head==None):
            return
        firstPoint = None
        toReturn=head
        for i in range(m - 1):
            firstPoint = head
            head = head.next
        first = head
        last = head
        lastPoint=last.next

        prev = None
        random = head
        for i in range(m, n + 1):
            if(i!=n):
                last = last.next
                lastPoint = last.next
            next = head.next
            head.next = prev
            prev = head
            if(i!=n):
                head = next

        random.next = lastPoint

        if(firstPoint):
            firstPoint.next = head
            return toReturn
        else:
            return head




ll1 = ListNode(1)
# ll1.next = ListNode(2)
# ll1.next.next = ListNode(3)
# ll1.next.next.next = ListNode(4)
# ll1.next.next.next.next = ListNode(5)
# ll1.next.next.next.next.next = ListNode(6)

var = Solution()
a=var.reverseBetween(ll1, 1, 1)

while (a):
    print(a.val)
    a = a.next
