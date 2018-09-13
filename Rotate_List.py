class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def rotateRight(self, head, k):
        a=self.calLength(head)
        length=a[0]
        lastNode=a[1]
        if(length==0):
            return
        k=k%length
        if(k==0):
            return head
        p=head
        for i in range(length-k-1):
            p=p.next
        back=p.next
        p.next=None
        lastNode.next=head

        return back

    def calLength(self, head):
        if(head==None):
            return [0, None]
        l=1
        while(head.next):
            l+=1
            head=head.next
        return [l, head]

ll1 = ListNode(1)
# ll1.next = ListNode(2)
# ll1.next.next = ListNode(3)
# ll1.next.next.next = ListNode(4)
# ll1.next.next.next.next = ListNode(5)
# ll1.next.next.next.next.next = ListNode(6)

var=Solution()
p=var.rotateRight(ll1, 2)

while(p):
    print(p.val)
    p=p.next
