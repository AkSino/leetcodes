class Tree():
    def __init__(self,val):
        self.right=None
        self.left=None
        self.val=val
class Solution():

    def largestValues(self, root):
        return self.maxElement(root,[0],0,[])

    def maxElement(self,root,array,n,answer):
        if not root:
            return
        if not root.right and not root.left:
            if array[n]>root.val:
                answer.append(array[n])
            else:
                answer.append(root.val)

        else:
            if n>=len(array)-1:
                if root.val<array[-1]:
                    array.append(array[-1])
                else:
                    array.append(root.val)
            else:
                if root.val<=array[-1]:
                    array[n]=array[-1]
                else:
                    array[n]=root.val
            self.maxElement(root.right,array,n+1,answer)
            self.maxElement(root.left,array,n+1,answer)

        return answer





