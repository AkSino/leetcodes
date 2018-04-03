# coding: utf-8

# # CODE FOR EXTRACTION OF INFORMATION FROM GOOGLE SCHOLAR

# In[1]:


# If nltk error comes up in this notebook please run the below commands otherwise ignore
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')


# ### ALL IMPORT HANDLING

# In[2]:


import operator
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from scipy.interpolate import spline
import re
import matplotlib.pyplot as plt;
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
import plotly.plotly as py
from math import sin
import sys
import nltk
from tinydb import TinyDB, Query
from collections import defaultdict

# ### ALL GLOBAL VARIABLES REQUIRED

# In[3]:


db = TinyDB('C:/users/varda/Onedrive/desktop/db_app.json')
stopWords = set(stopwords.words('english'))
dictionary = defaultdict(int)
query = Query()


# # DATABASE OPERATION STARTS

# ### UPDATE QUERY0

# In[4]:

def repetetiveMethod(db, sessionId, createOrNot):
    if createOrNot:
        createRun(db, sessionId)

    article_list = []
    response_list = []
    runId = len(db.search(query.sessionId == sessionId)[0]['runs'])
    dictionary = getWordDictionary(sessionId)
    docDict = getDocumentDictionary(sessionId)

    # rerepeat holds the top search queries for the next time
    rerepeat = chooseManualWords(sessionId, dictionary)
    updateQuery1(sessionId, rerepeat, runId)

    memoryWords = db.search(query.sessionId == sessionId)[0]['runs'][-1]['query1']

    origQuery = word_tokenize(db.search(query.sessionId == sessionId)[0]['query'].lower())

    flags = True
    arep = len(docDict)
    # arep is created to check if new documents comes in the cluster or not
    docNum = 0
    searchQuery1 = "+".join(memoryWords) + "+" + "+".join(rerepeat)
    searchQuery2 = "+".join(rerepeat)
    searchQuery3 = "+".join(origQuery) + "+" + "+".join(rerepeat)
    generated_urls1 = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=" + searchQuery1 + "&oq="
    generated_urls2 = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=" + searchQuery2 + "&oq="
    generated_urls3 = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=" + searchQuery3 + "&oq="
    for generated_url in [generated_urls1, generated_urls2, generated_urls3]:
        if flags == False:
            break
        mydivs = createSoup(generated_url).findAll("div", {"class": "gs_r gs_or gs_scl"})
        new_article_list = []
        new_response_list = []

        # Fetching the documents from the two search queries. If new_response_list(list containing new docs) is zero the it breaks
        for each in mydivs:
            cluster_id = fetch_cluster_id(each)
            if cluster_id not in docDict:
                docNum += 1
                new_article_list.append(
                    [fetch_article_title(each)[0], fetch_article_title(each)[1], fetch_cluster_id(each),
                     fetch_abstract(each), fetch_citation_detail(each)])
                new_response_list.append("EMPTY")

        # If no new document comes then continue to the next search
        if len(new_response_list) == 0:
            continue

        article_list += new_article_list
        response_list += new_response_list
        # Taking the response from the user
        flags = takeUserResponse(new_article_list, new_response_list, flags)

        # Update the weights of dictionary
        incrementDecrementWeight(new_article_list, new_response_list, dictionary, stopWords)

        # Setting the dictionary in Session and new docs in particular run
        setWordDictionary(db, dictionary, sessionId)

    docDict = arrayToDict(article_list, response_list)
    updateDocsInsideRuns(sessionId, docDict, runId)

    printBarGraph("Relevant vs Irrelevant Words", sessionId, db)
    createNewDocCountGraph(sessionId)

    arep = len(response_list) - arep
    if (flags and len(article_list) > 0):
        repetetiveMethod(db, sessionId, True)

def updateQuery0(db, sessionId, wordList, runId):
    dataStructure = db.search(query.sessionId == sessionId)
    c = (dataStructure[0]['runs'])

    for each in c:
        if each['runId'] == runId:
            each['query0'] = each['query0'] + wordList

    db.update({'runs': c}, query.sessionId == sessionId)
    db.search(query.sessionId == sessionId)


# ### UPDATE QUERY1

# In[5]:


def updateQuery1(sessionId, wordList, runId):
    dataStructure = db.search(query.sessionId == sessionId)
    c = list(dataStructure[0]['runs'])

    for each in c:
        if each['runId'] == runId:
            each['query1'] = wordList
            print(each)
    db.update({'runs': c}, query.sessionId == sessionId)
    db.search(query.sessionId == sessionId)


# ### GETTER FOR WORD LIST IN DICTIONARY FORM

# In[6]:


def getWordDictionary(sessionId):
    dataStructure = db.search(query.sessionId == sessionId)
    c = list(dataStructure[0]['wordlist'])
    wordDict = {}
    for each in c:
        wordDict[each['word']] = each['count']
    return wordDict


# ### SETTER FOR WORD LIST IN THE DATABASE FROM DICTIONARY

# In[7]:


def setWordDictionary(db, wordDict, sessionId):
    wordList = []
    for each in wordDict:
        newDict = {}
        newDict['count'] = wordDict[each]
        newDict['word'] = each
        wordList.append(newDict)
    db.update({'wordlist': wordList}, query.sessionId == sessionId)


# ### GETTER FOR DOCUMENTS FROM DATABASE

# In[8]:


def getDocumentDictionary(sessionId):
    dataStructure = db.search(query.sessionId == sessionId)
    c = list(dataStructure[0]['documents'])
    docDict = defaultdict(str)
    for each in c:
        docDict[each['cluster_id']] = each['response']
    return docDict


# ###  SETTER FOR DOCUMENT IN THE DATABASE FROM DUAL LIST

# In[9]:


def setDocumentDictionary(db, docDict, sessionId):
    docList = []
    for each in docDict:
        newDict = {}
        newDict['response'] = docDict[each]
        newDict['cluster_id'] = each
        docList.append(newDict)
    db.update({'documents': docList}, query.sessionId == sessionId)


# ### SETTING THE DOCUMENT INSIDE RUNS

# In[10]:


def updateDocsInsideRuns(sessionId, docDict, runId):
    docList = []
    for each in docDict:
        newDict = {}
        newDict['response'] = docDict[each]
        newDict['cluster_id'] = each
        docList.append(newDict)
    dataStructure = db.search(query.sessionId == sessionId)
    c = list(dataStructure[0]['runs'])
    c[-1]['docs'] = docList
    db.update({'runs': c}, query.sessionId == sessionId)


# ### SETTING THE STOPWORDS INSIDE THE SESSION

# In[11]:


def setStopWords(db, sessionId, listOfWords):
    dataStr = db.search(query.sessionId == sessionId)[0]['stopwords']
    dataStr += listOfWords
    db.update({'stopwords': dataStr}, query.sessionId == sessionId)


# ### CREATE NEW RUN ENTRY

# In[12]:


def createRun(db, sessionId):
    dataStructure = db.search(query.sessionId == sessionId)
    c = list(dataStructure[0]['runs'])
    p = dict(dataStructure[0]['runs'][-1])
    p['runId'] = p['runId'] + 1
    p['query0'] = p['query0'] + p['query1']
    p['query1'] = []
    p['docs'] = []
    db.update({'runs': c}, query.sessionId == sessionId)


# ### FETCHING USE TYPE(WORK ON NEW QUERY OR FETCH OLD QUERY DATA)

# In[13]:


login_type = input("You want to use create new query(Y) or use old(N)")
if (login_type == 'Y' or login_type == 'y'):
    firstTimeRun = True
    inputQuery = input("Please input your query")
    length = len(db)
    sessionId = length + 1
    db.insert(
        {"sessionId": sessionId, "query": inputQuery, "stopwords": list(stopWords), "wordlist": [], "documents": [],
         "runs": []})
    print("Your ID for this particular query is %d . Please save it for future reference" % (length + 1))
else:
    firstTimeRun = False
    sessionId = int(input("Please enter the ID"))
    createRun(db, sessionId)
    repetetiveMethod(db, sessionId, False)


# ### FOR PRINTING THE ARTICLE TITLE AND URL

# In[14]:


def fetch_article_title(data):
    mydivs = data.find("h3", {"class": "gs_rt"})
    try:
        return ([mydivs.text, mydivs.find('a').get('href')])
    except:
        return ([mydivs.text, "Cited"])


# ### FOR PRINTING THE ARTICLE ABSTRACT
#

# In[15]:


def fetch_abstract(data):
    for items in data.findAll("div", {"class": "gs_rs"}):
        if items.text:
            return (items.text)
        else:
            return "Cited"
    return "Cited"


# ### FOR GETTING THE CITATION LINK

# In[16]:


def fetch_citation_detail(data):
    mydivs = data.findAll("div", {"class": "gs_fl"})

    result = data.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['gs_fl'])
    for link in result[0].find_all('a'):
        answer = (link.get('href'))
        if "/scholar?cites" in answer:
            return ("https://scholar.google.com" + answer)


# ## CREATE BAR GRAPH

# In[17]:


def printBarGraph(title, sessionId, db):
    lastRun = db.search(query.sessionId == sessionId)['runs'][-1]['docs']
    objects = ('relevant', 'irrelevant')
    performance = [0, 0]
    for each in lastRun:
        if lastRun[each] == False:
            performance[1] += 1
        else:
            performance[0] += 1
    # objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    # performance = [10,8,6,4,2,1]
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title(title)
    plt.show()


# ### CREATE CURVED GRAPH FOR NEW DOCUMENTS

# In[18]:


def createNewDocCountGraph(sessionId):
    T = [0, 1]
    power = [0, 1]
    runs = db.search(query.sessionId == sessionId)['runs']
    for each in runs:
        T.append(T[-1] + 1)
        power.append(len(runs['docs']))

    T = np.array(T)
    power = np.array(power)
    xnew = np.linspace(T.min(), T.max(), 300)  # 300 represents number of points to make between T.min and T.max
    power_smooth = spline(T, power, xnew)
    plt.plot(xnew, power_smooth)
    plt.ylabel('# of new documents')
    plt.xlabel('Iteration Count')
    plt.title("Graph for new docs in each run")
    plt.show()


# ### FOR FETCHING THE CLUSTER ID OF PAPER

# In[19]:


def fetch_cluster_id(data):
    mydivs = data.findAll("div", {"class": "gs_fl"})

    result = data.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['gs_fl'])
    for link in result[0].find_all('a'):
        answer = (link.get('href'))
        if "/scholar?cites" in answer:
            answer = answer
            break
    args = answer.split('?', 1)[1]
    for arg in args.split('&'):
        if arg.startswith('cites='):
            cluster_id = arg[6:]
    return (cluster_id)


# ### FORMATION OF URL FROM USER INPUT

# In[20]:


if (firstTimeRun == True):
    # length+1 is the sessionId
    user_query_raw = db.search(query.sessionId == (sessionId))[0]['query']
    originalQueryTokenized = user_query_raw.lower().split()
    user_query = "+".join(user_query_raw.split())
    generated_url = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=" + user_query + "&oq="
    user_query_words = user_query.lower().split('+')


# ### CREATE SOUP FROM URL

# In[21]:


def createSoup(generated_url):
    req = Request(generated_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    return soup


# ### FOR CREATING THE ARRAY OF DETAILS OF ALL RESULTS FROM THE BASE PAGE

# In[22]:


if (firstTimeRun == True):
    mydivs = createSoup(generated_url).findAll("div", {"class": "gs_r gs_or gs_scl"})
    article_list = []
    response_list = []
    for each in mydivs:
        print(fetch_cluster_id(each))
        article_list.append(
            [fetch_article_title(each)[0], fetch_article_title(each)[1], fetch_cluster_id(each), fetch_abstract(each),
             fetch_citation_detail(each)])
        response_list.append(True)

# In[23]:


if (firstTimeRun == True):
    print("Please select the relevant pages. Respond with Y or N")
    n = 0
    for each in range(len(article_list)):
        n += 1
        print("Title:", end=" ")
        print(article_list[each][0])
        print("Abstract:", end=" ")
        print(article_list[each][3])
        response = input()
        print("#####################################################################################")
        if response == "N" or response == "n":
            response_list[each] = False
    docDictToFeed = {}
    for i in range(len(response_list)):
        docDictToFeed[article_list[i][2]] = response_list[i]

    setDocumentDictionary(db, docDictToFeed, sessionId)
    c = [{"runId": 1, "query0": [], "query1": [], "docs": []}]
    db.update({'runs': c}, query.sessionId == sessionId)
    updateQuery0(db, sessionId, originalQueryTokenized, 1)
    updateDocsInsideRuns(sessionId, docDictToFeed, 1)

# # CREATING DICTIONARY FOR WORD CORPUS

# In[26]:


if (firstTimeRun == True):
    for i in range(len(response_list)):
        a = article_list[i][0]
        b = article_list[i][3]
        # Taking out the words in the square brackets starts
        interim = []
        for each in a.split():
            if each[-1] != "]":
                interim.append(each)
        a = " ".join(interim)
        interim = []
        for each in b.split():
            if each[-1] != "]":
                interim.append(each)
        b = " ".join(interim)
        # Taking out the words in the square brackets ends
        a = re.sub(r'[^\w\s]', '', a)
        b = re.sub(r'[^\w\s]', '', b)
        title = word_tokenize(a.lower())
        abstract = word_tokenize(b.lower())
        ans = []
        if response_list[i] == True:
            for w in title:
                if w not in stopWords:
                    dictionary[w] += 1
        else:
            for w in title:
                if w not in stopWords:
                    dictionary[w] -= 1

    for each in dictionary:
        print(each, dictionary[each])
    setWordDictionary(db, dictionary, sessionId)


# In[25]:


def printMap(dictionary):
    X = np.arange(len(dictionary))
    pl.bar(X, dictionary.values(), align='center', width=0.5)
    pl.xticks(X, dictionary.keys())
    ymax = max(dictionary.values()) + 1
    ymin = min(dictionary.values()) - 1
    pl.ylim(ymin, ymax)
    pl.show()


# ### FIND MOST FREQUENT WORD

# In[25]:


def findMaxWord(dictionary):
    sorted_x = sorted(dictionary.items(), key=operator.itemgetter(1))
    maximum_rep = -10000
    rerepeat = []
    for i in reversed(sorted_x):
        if i[0] not in user_query_words:
            if i[1] >= maximum_rep:
                rerepeat.append(i[0])
                maximum_rep = i[1]
            else:
                break
    return (rerepeat)


def chooseManualWords(sessionId, dictionary):
    rerepeat = []
    sorted_x = sorted(dictionary.items(), key=operator.itemgetter(1))
    for i in reversed(sorted_x):
        print(i[0], i[1])
    print("For exiting please type exit")
    a = input()
    while a != "exit":
        rerepeat.append(a)
        a = input()

    setStopWords(db, sessionId, rerepeat)
    return rerepeat


if (firstTimeRun == True):
    dictionary = getWordDictionary(sessionId)
    # rerepeat=findMaxWord(dictionary)
    rerepeat = chooseManualWords(sessionId, dictionary)
    print(rerepeat)


# ### While all the words are done or user responds exit

# In[26]:


# We have user_query_words which stores the value of user query and we made rerepeat which is storing the values of top words that we are seaerching again


# In[27]:


# Take the response from the user
def takeUserResponse(new_article_list, new_response_list, flags):
    trueVal = 0
    falseVal = 0
    print("Please select the relevant pages. Respond with Y or N")
    for each in range(len(new_article_list)):
        if flags == False:
            break
        print("Title:", end=" ")
        print(new_article_list[each][0])
        print("Abstract:", end=" ")
        print(new_article_list[each][3])
        response = input()
        print("#####################################################################################")
        if response == "N" or response == "n":
            new_response_list[each] = False
            falseVal += 1

        # If user responds quit or exit, flag will be set to false and program will add those words to dictionary till where the user have given the input
        elif response.lower() == "quit" or response.lower() == "exit":
            flags = False
        elif response.lower() == "y" or response.lower() == "yes":
            new_response_list[each] = True
            trueVal += 1
    # Printing the relevant graphs
    return flags


# In[28]:


# Function for incrementing or decrementing the weight based on new responses
def incrementDecrementWeight(new_article_list, new_response_list, dictionary, stopWords):
    for i in range(len(new_response_list)):
        a = new_article_list[i][0]
        b = new_article_list[i][3]

        # Taking out the words in the square brackets starts
        interim = []
        for each in a.split():
            if each[-1] != "]":
                interim.append(each)
        a = " ".join(interim)
        interim = []
        for each in b.split():
            if each[-1] != "]":
                interim.append(each)
        b = " ".join(interim)
        # Taking out the words in the square brackets ends

        a = re.sub(r'[^\w\s]', '', a)
        b = re.sub(r'[^\w\s]', '', b)
        title = word_tokenize(a.lower())
        abstract = word_tokenize(b.lower())
        ans = []
        if new_response_list[i] == True:
            for w in title:
                if w not in stopWords:
                    dictionary[w] += 1
        elif new_response_list[i] == False:
            for w in title:
                if w not in stopWords:
                    dictionary[w] -= 1


# ### CONVERT ARRAY TO DICT

# In[29]:


def arrayToDict(articleList, responseList):
    docDicts = {}
    for i in range(len(articleList)):
        docDicts[articleList[i]] = responseList[i]
    return docDicts


# In[30]:




