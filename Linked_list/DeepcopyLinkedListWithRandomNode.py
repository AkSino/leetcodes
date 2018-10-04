class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        ret = RandomListNode(0)
        ret2 = ret
        count=0
        while head:
            # Create a new object for the next node
            ret.next = RandomListNode(head.label)

            # Move to the next node and set the random
            ret = ret.next
            if head.random:
                ret.random = RandomListNode(head.random.label)

            # Shift head to the next one
            head = head.next

        return ret2.next

a=RandomListNode(1)
a.next=RandomListNode(2)
c=RandomListNode(3)
a.next.next=c
a.random=c

var=Solution()
c=var.copyRandomList(a)