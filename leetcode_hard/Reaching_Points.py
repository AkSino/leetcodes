class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx
        return sx == tx and (ty - sy) % sx == 0 or sy == ty and (tx - sx) % sy == 0
var=Solution()
print(var.reachingPoints(0,3,3,3))























# class Solution(object):
#     def reachingPoints(self, sx, sy, tx, ty):
#         while tx>=sx and ty>=sy:
#             if tx==sx and ty==sy:
#                 return True
#             if tx>ty:
#                 tx=tx-ty
#             elif ty>tx:
#                 ty=ty-tx
#             elif ty==tx:
#                 if sx==0 and sy==ty:
#                     return True
#                 elif sy==0 and sx==tx:
#                     return True
#                 else:
#                     return False
#         return False
# var=Solution()
# print(var.reachingPoints(1,1,1000000000,1))

