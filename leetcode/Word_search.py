#https://leetcode.com/problems/word-search-ii/description/
def start_index(words,array,row,column):
    lists=[]
    initial=words[0]
    visited=[]
    for row in range(row):
        for column in range(column):
            if initial==array[row][column]:
               lists.append([[row][column]])
            visited[row][column]=False
    for i in lists:
        WordSearch(words, array, row, column, visited,1)


def WordSearch( words,array, row, column, visited,start_ind):
    check_word=words[start_ind]
    left=preciseSearch(row, column-1,check_word, array,visited)
    if left: visited[row][column-1]==True
    right = preciseSearch(row, column + 1, check_word, array, visited)
    if right: visited[row][column + 1] == True
    up = preciseSearch(row-1, column, check_word, array, visited)
    if up:
        visited[row-1][column] == True
        WordSearch()
    down = preciseSearch(row+1, column, check_word, array, visited)
    if down: visited[row+1][column] == True



def preciseSearch(row,column, letter, x,y,array, visited):
    if row<0 or column<0 or row>x or column>y or visited[row][column]==True:
        return False
    elif array[row][column]==letter:
        return True
    elif array[row][column]!=letter:
        return False




a=[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]


