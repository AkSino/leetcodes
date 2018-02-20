def checkIPs(ip_array):
    toReturn=[]
    for each in ip_array:
        i=0
        #If number if addresses are 8 then valid.
        if len(each.split(':')) == 8:
                for eachVal in each.split(':'):
                    # if there is nothing between dots then invalid
                    if eachVal == "":
                        i = 1
                        break
                    #If number more than 4 digit then invalid
                    if len(eachVal)>4:
                        i=1
                        break
                    #number should be a lowr/upper case from a-f or 0 to 9
                    for x in eachVal:
                        if  (48 <= ord(x) <= 57 or 65 <= ord(x) <= 70 or 97 <= ord(x) <= 102) == False:
                            i = 1
                if i == 0:
                    toReturn.append("IPv6")

        elif len(each.split('.'))==4:
            for item in each.split('.'):
                #i is used as a flag
                if i==1:
                    break
                # if there is nothing between dots then invalid
                if item=="":
                    i=1
                    continue
                # if first item is zero where more than one elements are present
                if len(item)>1 and item[0]=="0":
                    i=1
                    continue
                # If number is an integer then valid, else invalid
                if item.isdigit():
                    intVal=int(item)
                else:
                    i=1
                    continue
                # If number is out of range of 0 to 255 then invalid.
                if intVal < 0 or intVal > 255:
                    i=1
            if i==0:
                toReturn.append ("IPv4")
        else:
            i=1
        if i==1:
            toReturn.append("Neither")
    return toReturn