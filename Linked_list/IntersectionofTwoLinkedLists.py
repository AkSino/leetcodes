class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, head1, head2):
        l1=0
        l2=0
        headA=head1
        headB=head2
        while(headA):
            headA=headA.next
            l1+=1
        while(headB):
            headB=headB.next
            l2+=1

        if(l1>l2):
            diff=l1-l2
            while(diff>0):
                head1=head1.next
                diff-=1
        elif(l2>l1):
            diff=l2-l1
            while(diff>0):
                head2=head2.next
                diff-=1

        while(head1 and head2):
            if(head1.val == head2.val):
                return head2
            else:
                head2=head2.next
                head1=head1.next




