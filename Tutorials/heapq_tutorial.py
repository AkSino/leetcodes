#heapq is used as a priority queue. When we push elements in a queue and then pop the the elements, then elements smallest on the leftmost side will be popped
# out first and if they are equal then the second left element will be pooped out.


import heapq
import sys


a=[]

heapq.heappush(a,3)
heapq.heappush(a,5)
heapq.heappush(a,7)
heapq.heappush(a,1)

print(heapq.heappop(a))

b=[]

heapq.heappush(b,(7,(1,2)))
heapq.heappush(b,(4,(3,4)))
heapq.heappush(b,(1,(3,0)))
heapq.heappush(b,(100,(0,4)))

print(heapq.heappop(b))
print(heapq.heappop(b))
print(heapq.heappop(b))
print(heapq.heappop(b))