class Solution:
    def canVisitAllRooms(self, rooms):
        if (len(rooms) == 0):
            return True
        visited = [False for i in range(len(rooms))]
        visited[0] = True
        return self.helper(rooms, visited, 0, [1])

    def helper(self, rooms, visited, start, visits):
        if (visits[0] == len(rooms)):
            return True
        a = rooms[start]
        for each in a:
            if(not visited[each]):
                visited[each] = True
                visits[0] += 1
                if (self.helper(rooms, visited, each, visits)):
                    return True
        return False


var=Solution()
print(var.canVisitAllRooms([[1,7,9],[8,3,6],[1],[6,5],[4,7,7],[5,2,6],[4,5],[2],[9,8,2,3,4,8],[1,3,9]]))