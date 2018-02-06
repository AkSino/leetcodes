from collections import defaultdict
def groupAnagrams( strs):

    dic = defaultdict(list)
    for string in strs:
            dic[''.join(sorted(string))] += [string]

    return [value for key, value in dic.items()]


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))