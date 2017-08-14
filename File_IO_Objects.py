f=open("vardan.txt",'r')  #r stands for reading. There can be w, a(append), w+r etc
print(f.name)
f.close() #We have to close file manually otherwise it may lead to leaks and there can be more than the maximum allowed file descriptors which can cause error


#To avoid this manual closing of file we can user context manager as below:. File will be closed as soon as block completes

with open("vardan.txt",'r') as f:
    print(f.name)

#How to read the file
with open("vardan.txt",'r') as f:
    f_contents=f.read() #Reads complete file
    f_contents = f.read(100) #prints forst 100 chars and takes pointers to 100 place
    f_lines=f.readlines() #prints all the lines with \n depicting newline
    f_first_line=f.readline()#Reads the single line
    print(f_contents)
    print(f.tell()) #tells the position of pointer
    f.seek(0)  #Sets the posotion to 0
    while len(f_contents) > 0:
        print (f_contents)

    for line in f:    #Using for loop to read each line of file
        print (line)

#write to a file
with open("test.txt",'w') as f:
    f.write("Vardan")   #It will overwrite if file already exist. If we dont want to overwrite the file then use a instead of w.
    f.write("Gupta")
    f.seek(0) #Reposition curson to 0 and again the file will be rewritten from scratch.


#Code to copy content of one file to other

with open('vardan.txt','r') as rf:
    with open('test2.txt','w') as wf:
        for line in rf:
            wf.write(line)

#If we want to work with the images then simply add b after the r and w as below.
with open('vardan.jpg','rb') as rf:
    with open('test2.jpg','wb') as wf:
        for line in rf:
            wf.write(line)