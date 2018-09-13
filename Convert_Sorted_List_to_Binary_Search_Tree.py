class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        array = []
        while head:
            array.append(head.val)
            head = head.next
        self.arrayToTree(array, 0, len(array) - 1)

    def arrayToTree(self, array, start, end):
        if(start == end):
            return TreeNode(array[start])
        mid = (start + end) // 2
        root = TreeNode(array[mid])
        root.left = self.arrayToTree(array, 0, mid - 1)
        root.right = self.arrayToTree(array, mid+1, len(array) - 1)

def arrayToLinkedList()
