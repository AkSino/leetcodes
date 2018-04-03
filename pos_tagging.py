from nltk.corpus import stopwords
import nltk
import os

import re


stopWords = set(stopwords.words('english'))

print(stopWords)

print('can' in stopWords)
array=[]
name="Can you lend me the book"
name.lower()
name = re.sub(r'[^\w\s]', '', name)
input_text=name
text = nltk.word_tokenize(input_text)
print(text)
for each in text:
    if each.lower() not in stopWords:
        array.append(each.lower())
result=nltk.pos_tag(text)
print(array)
