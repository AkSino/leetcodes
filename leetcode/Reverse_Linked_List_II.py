class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class Solution:
    def reverseBetween(self, head, m, n):
        prev=None
        if head==None:
            return
        current=head

        for i in range(m-1):
            prev=current
            current=current.next
        next=current.next
        for j in range(m,n):
            
a=Node(1)
a.next=Node(2)
a.next.next=Node(3)
a.next.next.next=Node(4)
a.next.next.next.next=Node(5)
var=Solution()
m=var.reverseBetween(a,2,3)
print(m.data,m.next.data,m.next.next.data)
