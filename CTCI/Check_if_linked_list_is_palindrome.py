class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
def checkPalindrome(root):
    slow = root
    fast = root
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    back=slow
    slow = slow.next
    prev=None
    current=slow
    while current:
        next = current.next
        current.next=prev
        prev=current
        current=next
    back.next=prev
    return root
a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)
a.next.next.next.next=Node(5)
ll=(checkPalindrome(a))
while ll:
    print(ll.data)
    ll=ll.next

