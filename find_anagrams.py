def find_anaram(character):
    if len(character)==1:
        return [character[0]]
    for i in range(len(character)):
        character[0],character[i]=character[i],character[0]
        print([character[0]]+find_anaram(character[1:len(character)]))
        character[0], character[i] = character[i], character[0]

find_anaram(["v","a","r"])