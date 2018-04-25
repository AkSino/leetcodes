import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def __eq__(self, other):
        return self.intAttribute == other.intAttribute
    def mergeKLists(self, lists):
        if lists == [[]]:
            return None
        if len(lists) == 0:
            return None
        arr = []
        ans = ListNode("Dummy")
        start = ListNode("0")
        ans.next = start
        for i in range(len(lists)):
            if (lists[i]):
                heapq.heappush(arr, [lists[i].val, lists[i]])
        if len(arr) == 0:
            return None
        while arr:
            a = heapq.heappop(arr)
            start.next = ListNode(a[0])
            start = start.next
            if a[1].next:
                a[1] = a[1].next
                heapq.heappush(arr, [a[1].val, a[1]])
        return ans.next.next


var1=ListNode(1)
var1.next=ListNode(2)
var1.next.next=ListNode(2)
var2=ListNode(1)
var2.next=ListNode(1)
var2.next.next=ListNode(2)

ques=Solution()
node=ques.mergeKLists([var1,var2])
print(node.val,node.next.val,node.next.next.val,node.next.next.next.val)