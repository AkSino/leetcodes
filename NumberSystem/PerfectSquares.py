class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sq=[]
        i=1
        while i*i<=n:
            sq.append(i*i)
            i+=1
        if n in sq:
            return 1
        else:
            for x in sq:
                if n-x in sq:
                    return 2
        sq2=[]
        for x in sq:
            for y in sq:
                sq2.append(x+y)
        for x in sq:
            if n-x in sq2:
                return 3
        return 4