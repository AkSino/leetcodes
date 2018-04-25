class Solution:
    def fullJustify(self, words, maxWidth):
        width=0
        count=len(words[0])
        ans=[]
        string=words[0]
        start=0
        end=0
        lenWords=0
        for i in range(len(words)):
            if count+len(words[i+1])+1>maxWidth:
                for i in range(start+1,end+1):
                    dist = -(-(maxWidth - lenWords) // (end - start))

            else:
                string+=" "

