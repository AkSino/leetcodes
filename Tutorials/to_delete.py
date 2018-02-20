
from __future__ import print_function

from keras.models import Sequential, Model
from keras.layers.embeddings import Embedding
from keras.layers import Input, Activation, Dense, Permute, Dropout, add, dot, concatenate
from keras.layers import LSTM
from keras.utils.data_utils import get_file
from keras.preprocessing.sequence import pad_sequences
from functools import reduce
import tarfile
import numpy as np
import re


def tokenize(sent):
    '''Return the tokens of a sentence including punctuation.
    >>> tokenize('Bob dropped the apple. Where is the apple?')
    ['Block', 'chain', 'is ', 'good', '.', ]
    '''
    return [x.strip() for x in re.split('(\W+)?', sent) if x.strip()]


def parsingSet(lines, support=False):
    data = []
    dataStory = []
    for eachLine in lines:
        eachLine = eachLine.decode('utf-8').strip()
        nid, eachLine = eachLine.split(' ', 1)
        nid = int(nid)
        if nid == 1:
            dataStory = []
        if '\t' in eachLine:
            q, a, supportData = eachLine.split('\t')
            q = tokenize(q)
            subSet = None
            if support:
                supportData = map(int, supportData.split())
                subSet = [dataStory[i - 1] for i in supportData]
            else:
                subSet = [x for x in dataStory if x]
            data.append((subSet, q, a))
            dataStory.append('')
        else:
            sent = tokenize(eachLine)
            dataStory.append(sent)
    return data


def getData(f, only_supporting=False, max_length=None):
    data = parsingSet(f.readlines(), support=only_supporting)
    flattenedSet = lambda data: reduce(lambda x, y: x + y, data)
    data = [(flattenedSet(story), q, answer) for story, q, answer in data if not max_length or len(flattenedSet(story)) < max_length]
    return data


def vectorize_stories(data, words, story_maxlen, query_maxlen):
    X = []
    Xq = []
    Y = []
    for story, query, answer in data:
        x = [words[w] for w in story]
        xq = [words[w] for w in query]
        y = np.zeros(len(words) + 1)
        y[words[answer]] = 1
        X.append(x)
        Xq.append(xq)
        Y.append(y)
    return (pad_sequences(X, maxlen=story_maxlen),
            pad_sequences(Xq, maxlen=query_maxlen), np.array(Y))
with open("dataset.txt", 'r') as f:
    path = f.read()
tar = tarfile.open(path)

possibleQues = {
    'single_supporting_fact_10k': 'tasks_1-20_v1-2/en-10k/qa1_single-supporting-fact_{}.txt',
}
quesType = 'single_supporting_fact_10k'
challenge = possibleQues[quesType]

print('Extracting stories for the challenge:', quesType)
train_stories = getData(tar.extractfile(challenge.format('train')))
test_stories = getData(tar.extractfile(challenge.format('test')))

vocab = set()
for story, q, answer in train_stories + test_stories:
    vocab |= set(story + q + [answer])
vocab = sorted(vocab)
vocab_size = len(vocab) + 1
story_maxlen = max(map(len, (x for x, _, _ in train_stories + test_stories)))
query_maxlen = max(map(len, (x for _, x, _ in train_stories + test_stories)))

print('-')
print('Vocab size:', vocab_size, 'unique words')
print('Story max length:', story_maxlen, 'words')
print('Query max length:', query_maxlen, 'words')
print('Number of training stories:', len(train_stories))
print('Number of test stories:', len(test_stories))
print('-')
print('Here\'s what a "story" tuple looks like (input, query, answer):')
print(train_stories[0])
print('-')
print('Vectorizing the word sequences...')

word_idx = dict((c, i + 1) for i, c in enumerate(vocab))
inputs_train, queries_train, answers_train = vectorize_stories(train_stories,
                                                               word_idx,
                                                               story_maxlen,
                                                               query_maxlen)
inputs_test, queries_test, answers_test = vectorize_stories(test_stories,
                                                            word_idx,
                                                            story_maxlen,
                                                            query_maxlen)

print('-')
print('inputs: integer tensor of shape (samples, max_length)')
print('inputs_train shape:', inputs_train.shape)
print('inputs_test shape:', inputs_test.shape)
print('-')
print('queries: integer tensor of shape (samples, max_length)')
print('queries_train shape:', queries_train.shape)
print('queries_test shape:', queries_test.shape)
print('-')
print('answers: binary (1 or 0) tensor of shape (samples, vocab_size)')
print('answers_train shape:', answers_train.shape)
print('answers_test shape:', answers_test.shape)
print('-')
print('Compiling...')
input_sequence = Input((story_maxlen,))
question = Input((query_maxlen,))
input_encoder_m = Sequential()
input_encoder_m.add(Embedding(input_dim=vocab_size,
                              output_dim=64))
input_encoder_m.add(Dropout(0.3))
input_encoder_c = Sequential()
input_encoder_c.add(Embedding(input_dim=vocab_size,
                              output_dim=query_maxlen))
input_encoder_c.add(Dropout(0.3))
question_encoder = Sequential()
question_encoder.add(Embedding(input_dim=vocab_size,
                               output_dim=64,
                               input_length=query_maxlen))
question_encoder.add(Dropout(0.3))
input_encoded_m = input_encoder_m(input_sequence)
input_encoded_c = input_encoder_c(input_sequence)
question_encoded = question_encoder(question)

match = dot([input_encoded_m, question_encoded], axes=(2, 2))
match = Activation('softmax')(match)

response = add([match, input_encoded_c])
response = Permute((2, 1))(response)

answer = concatenate([response, question_encoded])

answer = LSTM(32)(answer)

answer = Dropout(0.3)(answer)
answer = Dense(vocab_size)(answer)
answer = Activation('softmax')(answer)

model = Model([input_sequence, question], answer)
model.compile(optimizer='rmsprop', loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit([inputs_train, queries_train], answers_train,
          batch_size=32,
          epochs=120,
          validation_data=([inputs_test, queries_test], answers_test))