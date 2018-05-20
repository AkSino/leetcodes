class Solution:
    def uniqueMorseRepresentations(self, words):
        array=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dict={}
        count=0
        for each in words:
            ans=""
            for char in each:
                ans+=array[ord(char)-ord("a")]

            if ans in dict:
                dict[ans]+=1
            else:
                dict[ans]=0
                count+=1
        return count

