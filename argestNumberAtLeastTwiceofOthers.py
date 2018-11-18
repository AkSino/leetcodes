import sys


class Solution(object):
    def dominantIndex(self, nums):
        first = -sys.maxint
        second = -sys.maxint
        index=-1
        count=-1
        for each in nums:
            count+=1
            if(each>first):
                second = first
                first = each
                index=count
            elif(each>second):
                second=each

        if(first>=2*second):
            return index

        else:
            return -1