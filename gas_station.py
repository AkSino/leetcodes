class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1
        else:
            n=len(gas)
            i,total=0,0
            while i<n:
                if gas[i]-cost[i]>=0:
                    start=i
                    while total>=0 and i<n:
                        total+=gas[i]-cost[i]
                        i+=1
                        if total<0:
                            total=0
                            break
                else:
                    i+=1
            return start