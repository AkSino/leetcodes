from collections import Counter
import heapq

#Concept of this question is that we will start arranging in order of decreasing count of numbers.
# Firstly we will arrange all the numbers with max count and decide what can be number of free slots.
#Then we start filling out those slots.

class Solution(object):
    def leastInterval(self,tasks,n):
        data = Counter(tasks)
        hq = [-c for c in data.values()]
        heapq.heapify(hq)
        #Subtracting 1 because we will not be considering spaces in from if last digit
        maxValues = -heapq.heappop(hq)-1
        #Therefore idle slots will be
        idleSlotes = maxValues*n

        while hq:

            value = -heapq.heappop(hq)
            idleSlotes -= min(maxValues,value)

        return idleSlotes+len(tasks) if idleSlotes > 0 else len(tasks)


var = Solution()
print(var.leastInterval(["A","A","A","A","A","A","B","B","B","B","B","B"], 2))


a=[]
a.in