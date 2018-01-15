class Node():
    def __init__(self,data):
        self.data=data
        self.next=None


class Solution():
    def swapPairs(self, head):
        pre=Node("jbj")
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return pre.next



a=Node(1)
a.next=Node(2)
a.next.next=Node(3)
a.next.next.next=Node(4)
a.next.next.next.next=Node(5)
var=Solution()
m=var.swapPairs(a)
print(m.data,m.next.data,m.next.next.data)

import nltk
