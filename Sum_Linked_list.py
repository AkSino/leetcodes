class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

def sumList(l1,l2):
    first=l1
    second=ll2
    carry=0
    prev=None
    while first or carry:
        if first:
            a=first.data
            b=second.data
            ans=(a+b+carry)%10
            carry=(a+b)//10
            node=Node(ans)
            if prev:
                prev.next=node
                prev=node
            else:
                prev=node
                ret=prev
            first=first.next
            second=second.next
        else:
            node=Node(carry)
            prev.next=node
            return ret

    return ret




ll1=Node(2)
ll1.next=Node(3)
ll1.next.next=Node(4)

ll2=Node(2)
ll2.next=Node(5)
ll2.next.next=Node(9)

ll=(sumList(ll1,ll2))

while ll:
    print(ll.data)
    ll=ll.next