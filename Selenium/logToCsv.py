with open("C:\\Users\\varda\\OneDrive\\Desktop\\testing.txt",'r') as f:
    line = f.readline()

columns=5
count=0
with open("C:\\Users\\varda\\OneDrive\\Desktop\\testing.csv",'w') as f:
    for each in line:
        count+=1
        if(count==columns):
            f.write(each+","+ "\n")
            count=0
        else:
            f.write(each + ",")

