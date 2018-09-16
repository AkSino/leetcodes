#https://leetcode.com/problems/task-scheduler/description/

from collections import defaultdict

class Solution:
    def leastInterval(self, tasks, n):
        tasks=[]
        tasks.sort()
        dict=defaultdict(str)


