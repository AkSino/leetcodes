def Possible(arra):
    for i in range(len(arra)-1):
        if (arra[i]==arra[i+1]):
            return False
    else:
        return True

def distinct(Stra):
    arra = list(Stra)
    mains=[]
    for i in range(len(arra)):
        if arra[i] not in mains:
            mains.append(arra[i])
    return mains

data="muqxvjuhhfyrdiwzziekspbukmnkpzyarxmdvuyqaizwcavfhodjlpqajdbdpexljtfxlvbfvlvfpgjnubofvyqmulpakgywoepkfaqmoaevbvputhnvforjcqlaedetfgkpbkkwnymwjhvfdmnababoonozwfogycbxcubvexonqlbiypvlhlcyezdudtnrgejbzrrsybdyjcohbraerbqiktmkkqapiaezcbyzposzickmgecbequfrpocmixublhqjquvzigrwzvsfmkqktzpeaufivthktpjvnubwebyrxdqklorkqnozbdq"
nor=list(data)
converted=distinct(data)
max_data=[]
con_string=[]
for i in range(len(converted)-1):
    for m in range(i+1,len(converted)):
        fir=converted[i]
        sec=converted[m]
        for j in range(len(nor)):
            if nor[j]==fir or nor[j]==sec:
                con_string.append(nor[j])
        if Possible(con_string)==True:
            max_data.append(len(con_string))
        if not Possible(con_string)==False:
            pass
        con_string=[]
if max_data:
    print(max(max_data))
if not max_data:
    print("0")



