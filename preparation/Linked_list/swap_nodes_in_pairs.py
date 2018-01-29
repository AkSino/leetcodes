class Node():
    def __init__(self,data):
        self.data=data
        self.next=None


def reverseInPairs( head):
    dummy = p = Node(0)
    dummy.next = head
    while head and head.next:
        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        p.next = tmp
        head = head.next
        p = tmp.next
    return dummy.next


# Recursively
# def reverseInPairs(head):
#     if head and head.next:
#         tmp = head.next
#         head.next = reverseInPairs(tmp.next)
#         tmp.next = head
#         return tmp
#     return head
a=Node(1)
a.next=Node(2)
a.next.next=Node(3)

m=reverseInPairs(a)
while m:
    print(m.data)
    m=m.next
