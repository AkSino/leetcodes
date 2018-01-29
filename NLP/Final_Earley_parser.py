from collections import defaultdict
from re import findall, search, split, sub, match
import fileinput
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import sys

inputGrammar = defaultdict(list)
pos = set()


def wordCat(wordPut):  # get the type of word after input is being processed by tokenizer
    if match('^[-+]?[0-9]+$', wordPut):
        return "INT"
    elif match('[+-]?([0-9]*[.])?[0-9]+', wordPut):
        return "DOUBLE"
    elif match('\W', wordPut):
        return "OP"
    elif type('\w') is str:
        return "STRING"


def fetchRight(string):  # get the rhs of the rule
    pat_match_left = search(r'\^\s*(.*)\b', string)
    if pat_match_left:
        return pat_match_left.group(1).split()[0]
    else:
        return 0


def predictor(row_input):
    rhs = fetchRight(row_input[0])
    lhs = fetchLeft(row_input[0])
    if lhs not in pos:
        for each in inputGrammar[rhs]:
            to_append = [rhs + " -> " + " ^ " + each, row_input[2], row_input[2], "Predictor"]
            if to_append not in s[row_input[2]]:
                enqueue(row_input[2], to_append)


def fetchLeft(string):
    pat_match_left = findall(r'(?:^|(?:[->?!]\s))([a-zA-Z]+)', string)
    if pat_match_left:
        returnOutput = pat_match_left[0].strip()
        return returnOutput
    else:
        print(string[0])


def completer(row_input):  # increments one step when a match is found by the scanner
    lhs = fetchLeft(row_input[0])
    for each in s[row_input[1]]:
        if ("^" + " " + lhs) in each[0] and lhs != "S":
            left = each[0].split('^')[0]
            right = each[0].split('^')[1]
            mid = right.split(" ")[1]
            to_append = [left + mid + " ^ " + " ".join(right.split()[1:]), each[1], row_input[2], "Completer"]
            enqueue(row_input[2], to_append)


def wordCat(input_token):  # get the type of word after input is being processed by tokenizer
    if match('^[-+]?[0-9]+$', input_token):
        return "INT"
    elif match('[+-]?([0-9]*[.])?[0-9]+', input_token):
        return "DOUBLE"
    elif match('\W', input_token):
        return "OP"
    elif type('\w') is str:
        return "STRING"


def scanner(row_input, i):  # scans the input word so as to get a match with the parts of speech
    fetched = fetchRight(row_input[0])
    if i < len(inputGrammar["W"]) and inputGrammar["W"][i] in inputGrammar[fetched]:
        to_append = [fetched + " -> " + inputGrammar["W"][i] + " ^ ", row_input[2], row_input[2] + 1, "Scanner"]
        enqueue(row_input[2] + 1, to_append)


def earley_parser(
        words):  # Initialize a dummy state and calls predictor, scanner and completer to give the final result
    enqueue(0, ["Z -> ^ S", 0, 0, "Dummy Start State"])
    for i in range(len(words) + 1):
        for row_input in s[i]:
            rhs = fetchRight(row_input[0])
            if rhs != 0 and rhs not in pos:
                predictor(row_input)
            elif rhs != 0 and rhs in pos:
                scanner(row_input, i)
            else:
                completer(row_input)


def enqueue(state, chart_entry):
    i = 0
    for item in s[state]:
        if item[0] == chart_entry[0]:
            i = 1
    if i == 0:
        s[state].append(chart_entry)


def main_method():
    ps = PorterStemmer()
    inputPattern = ""
    array = []
    count = var1 = var2 = second_char = First_char = 0
    for inputSys in fileinput.input():
        for w in word_tokenize(inputSys):
            if count == 0:
                print("\nStemmer: ")
                count += 1
            type_of_word = wordCat(w)
            if inputSys.find('=') == -1:
                if search('\|\s([a-zA-Z\-\s]+)', w):
                    partsCode = split('\|', w)
                    for i in range(len(partsCode)):
                        if len(partsCode) > 1 and i == 1 and partsCode[i] is not '':
                            print('|', ' ', 'OP', ' ', fileinput.lineno())
                        if partsCode[i] is '':
                            print('|', ' ', 'OP', ' ', fileinput.lineno())
                        else:
                            type_of_word = wordCat(partsCode[i])
                            print(partsCode[i], ' ', type_of_word, ' ', fileinput.lineno())
                else:
                    print(w, ' ', type_of_word, ' ', fileinput.lineno())
            else:
                if search('[A-Za-z]', w) and w != "W":
                    print(w, ' ', type_of_word, ' ', fileinput.lineno(), ' ', ps.stem(w).lower(), ' ')
                else:
                    print(w, ' ', type_of_word, ' ', fileinput.lineno())
        inputSys.strip()
        if "#" in inputSys:
            continue
        if inputPattern and inputPattern[-1] == ";":
            array.append(inputPattern)
            inputPattern = ""
        if inputSys and inputSys[-1] == ";":
            inputPattern = inputPattern + inputSys
            array.append(inputPattern)
            inputPattern = ""
        elif ":" in inputSys:
            if inputPattern:
                array.append(inputPattern)
            inputPattern = inputSys
        else:
            inputPattern += inputSys
    if inputPattern:
        array.append(inputPattern)
    for line in array:
        sent = search('[^(a-zA-Z|\*|\s|\:|\=|\;|\-|\||\#|\.|\?|\!|\,|\'|\")]', line)
        if sent is not None and sent.group(0):
            print("Invalid")
            exit("Invalid")
        elif line.isspace():
            continue

        First_char = var2 + line.count(';')
        second_char = var1 + line.count(':')
        if First_char == second_char:
            First_char = second_char = var2 = var1 = 0
        elif First_char > second_char:
            print("Error in input")
            sys.exit("Error in input")
        else:
            var1 = second_char
            var2 = First_char

        for pick in line.split(';'):
            pick = pick.lstrip()
            if search('^([a-zA-Z\-]+)\s*[\:|\=]+\s*([a-zA-Z\-\|\\s\'\"\,\.\?\!]*)', pick):
                parts = search('([a-zA-Z\-]+)\s*[\:|\=]+\s*([a-zA-Z\-\|\\s\'\"\,\.\?\!]*)', pick)
                leftSide = parts.group(1)
                if parts.group(2).find('|') == -1 and leftSide == 'W':
                    ssp = split('\s+', parts.group(2))
                else:
                    ssp = split('\s*\|\s*', parts.group(2))
            elif findall('\s*\|\s*[a-zA-Z\-\s]+', pick):
                ccp = findall('\s*\|\s*([a-zA-Z\-\s]+)', pick)
                for x in ccp:
                    basePart = x
                    basePart = sub('[\n\t\r]+', ' ', basePart)
                    inputGrammar[leftSide].append(basePart.rstrip())
            elif search('\#\s*[a-zA-Z]+', pick):
                continue

            for i in range(len(ssp)):
                if ssp[i].islower():
                    if leftSide != 'W':
                        pos.add(leftSide)
                if leftSide == 'W':
                    a = search('[a-zA-Z\-]+', ssp[i])
                    if ssp[i] == '' or a is None:
                        continue
                    b = a.group(0)
                    rightWord = ps.stem(b).lower()
                else:
                    rightWord = ssp[i]
                    rightWord = sub('[\n\t\r]+', ' ', rightWord)
                inputGrammar[leftSide].append(rightWord.rstrip())

    if First_char < second_char:
        print("Error in Input")
        sys.exit("Error in Input")
    print("ENDFILE")
    if not inputGrammar or 'W' not in inputGrammar:
        print("Please Input Data")
        sys.exit("Please Input Data")


def createChart():
    print("\nParsed Chart: ")
    chart_number = check_chart = 0
    for each in s:
        for elem in each:
            if check_chart == elem[2]:
                print("\nChart [", elem[2], "]")
                check_chart += 1
            print("{:<30s} {:>30s} {:>30s}".format("S" + str(chart_number) + " " + elem[0], str([elem[1], elem[2]]),elem[-1]))
            chart_number += 1


def BaseClass(words):
    global s
    s = [[] for i in range(len(words) + 1)]
    for word in inputGrammar["W"]:
        found = 0
        for x in inputGrammar:
            if x != "W":
                for j in inputGrammar[x]:
                    if j == word:
                        found += 1

        if found == 0:
            print("Incorrect Input")
            exit("Incorrect Input")
    earley_parser(inputGrammar["W"])


main_method()
BaseClass(inputGrammar["W"])
createChart()
