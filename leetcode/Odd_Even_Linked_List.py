from Linked_list_node import Node

class Solution():
    def oddEvenList(self,head):
        ans=head
        even=head
        ress=1
        ress2=1
        odd=head.next
        odd_ans=head.next
        while even or odd:
            if even and even.next and even.next.next:
                    even.next=even.next.next
                    even=even.next
            else:
                ress=0
            if odd and odd.next and odd.next.next:
                    odd.next=odd.next.next
                    odd=odd.next
            else:
                ress2=0

            if ress==0 and ress2==0:
                even.next=odd_ans
                return ans


var=Node(1)
# var.next=Node(2)
# var.next.next=Node(3)
# var.next.next.next=Node(4)

vardan=Solution()
ans=vardan.oddEvenList(var)
while ans:
    print(ans.data)
    ans=ans.next