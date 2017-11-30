#https://leetcode.com/problems/accounts-merge/description/

accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"]]

visited=[[[False] for i in range(len(accounts))]]
result=[]
print(visited)
for i in range(len(visited)):

