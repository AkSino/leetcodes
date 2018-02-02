from nltk import word_tokenize
from collections import Counter
from nltk import ngrams

def ngram(input):
    ans=""
    for each in input:
        if 65<=ord(each)<=90 or 97<=ord(each)<=122 or each==" " or 48<=ord(each)<=57:
            ans+=each
    m,j=0,0
    splitWords=[]
    splitWords = splitWords + word_tokenize(ans.lower())
    length = len(splitWords)
    setting=set(splitWords)
    print("Probability of Unigram")
    for each in setting:
        uni = splitWords.count(each) / length
        print(each + ":" + str(uni))
    each=0
    ele=1
    ngrams=(ans.split())
    list_of_bigram=[]
    while ele<len(ngrams):
        list_of_bigram.append((ngrams[each], ngrams[ele]))
        each+=1
        ele+=1
    freqb = Counter(list_of_bigram)

    print("\nProbability for Bigram")
    while j < len(list_of_bigram):
        print(str(list_of_bigram[j]) + ":" + str((freqb[list_of_bigram[j]]) / splitWords.count(splitWords[m])))
        m+=1
        j+=1

ngram('can you tell me about any good cantonese restaurants. close by \
mid priced thai food is what im looking for \
tell me about chez panisse tell me tell about tell it')