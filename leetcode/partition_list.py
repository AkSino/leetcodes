from Linked_list_node import Node
class Solution:
    def partition(self, head, x):
        h1 = l1 = Node(0)
        h2 = l2 = Node(0)
        while head:
            if head.data < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next

lis=Node(2)
lis.next=Node(4)
lis.next.next=Node(2)
lis.next.next.next=Node(1)
lis.next.next.next.next=Node(5)

var=Solution()
a=var.partition(lis,3)
while a:
    print(a.data)
    a=a.next
