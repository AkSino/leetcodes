from nltk import PorterStemmer
ps=PorterStemmer()
def checkInt(str):
    try:
        int(str)
        return True
    except:
        return False
with open("input_file",'r') as f:
    ans=f.read().splitlines()
    count=0
    for i in ans:
        count += 1
        stri = i.split()
        symbols = [":", ".", "|", ";"]
        if i[:3]!="W =":
            for each in stri:
                if len(each)==1 and each in symbols:
                    print(each, "OP", count )
                elif checkInt(each):
                    print(each, "INT",count)
                else:
                    print(each, "STRING",count)
        else:
            for j in range(len(stri)):
                if j<2:
                    if len(stri[j]) == 1 and stri[j] in symbols:
                        print(stri[j], "OP", count)
                    elif checkInt(stri[j]):
                        print(stri[j], "INT", count)
                    else:
                        print(stri[j], "STRING", count)
                else:
                    if stri[j][-1]==".":
                        stri=stri[j][0:-1]
                        if len(stri) == 1 and stri in symbols:
                            print(stri, "OP", count, ps.stem(stri))
                        elif checkInt(stri[j]):
                            print(stri, "INT", count, ps.stem(stri))
                        else:
                            print(stri, "STRING", count, ps.stem(stri))
                        print(".","OP",count)
                    else:
                        if len(stri[j]) == 1 and stri[j] in symbols:
                            print(stri[j], "OP", count,ps.stem(stri[j]))
                        elif checkInt(stri[j]):
                            print(stri[j], "INT", count,ps.stem(stri[j]))
                        else:
                            print(stri[j], "STRING", count,ps.stem(stri[j]))




