class Solution(object):
    def compareVersion(self, version1, version2):
        array1 = version1.split(".")
        array2 = version2.split(".")

        mini = min(len(array1), len(array2))
        i=0

        while(i<len(array1)):
            if(i==len(array2)):
                while(i<len(array1)):
                    if(int(array1[i])>0):
                        return 1
                    i+=1
                break
            if (int(array1[i]) > int(array2[i])):
                return 1
            elif (int(array1[i]) < int(array2[i])):
                return -1
            else:
                i+=1
                continue
        while(i<len(array2)):
            if (int(array2[i]) > 0):
                return -1
            i+=1
        return 0



var=Solution()
print(var.compareVersion("1.0", "1"))