from Linked_list_node import Node

class Solution():
    def mergeList(self,head1,head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        if head1.data<=head2.data:
            node=head1
            head1.next=self.mergeList(head1.next,head2)
        else:
            node=head2
            head2.next=self.mergeList(head1,head2.next)

        return node

var=Node(1)
var.next=Node(5)
var.next.next=Node(9)

gup=Node(3)
gup.next=Node(7)
gup.next.next=Node(11)

a=Solution()
ans=a.mergeList(var,gup)

while ans:
    print(ans.data)
    ans=ans.next
