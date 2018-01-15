class Solution():
    def groupAnagrams(self, strs):
        hash={}
        for val,each in enumerate(strs):
            a="".join(sorted(each))
            if a in hash:
                hash[a].append(each)
            else:
                hash[a]=[each]

        result = []
        for value in hash.values():
            result += [sorted(value)]
        return result

var=Solution()
print(var.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
