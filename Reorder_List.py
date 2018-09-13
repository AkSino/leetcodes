class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head):
        if(head)
        self.halfList(head)
        while (head):
            print(head.val)
            head = head.next

    def halfList(self, head):
        slowPointer = head
        fastPointer = head
        mem = slowPointer

        while fastPointer and fastPointer.next:
            mem = slowPointer
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        head2 = self.opposeList(slowPointer)

        mem.next = None
        next1 = head.next
        next2 = head2.next


        while (head and head2):
            if (head.next == None and head2.next):
                head.next = head2
                break
            elif(head2.next==None and head.next==None):
                head.next = head2
                break
            head.next = head2
            head2.next = next1
            head = next1
            head2 = next2
            next1=head.next
            next2=head2.next


    def opposeList(self, root):
        dummy = None
        while (root):
            next = root.next
            root.next = dummy
            dummy = root
            if (next):
                root = next
            else:
                break
        return root


ll1 = ListNode(1)
ll1.next = ListNode(2)
ll1.next.next = ListNode(3)
ll1.next.next.next = ListNode(4)
# ll1.next.next.next.next = ListNode(5)
# ll1.next.next.next.next.next = ListNode(6)
var = Solution()
var.reorderList(ll1)
