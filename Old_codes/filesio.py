import os   #Renaming and removing done by this only in the last part of the code


reader=open("D:\\files.txt","r+")
reader.write("jjiji")
position=reader.tell()  #Tells the position of pointer at current time
print position
reader.seek(2)  #Changes the position of cursor to mentioned point
position=reader.tell()
strings=reader.read() #Will return full file starting from pointer location
strings=reader.readline() #Will return the current line
strings2=reader.readlines() #Will return the full file in list format
print position
print strings
print strings2
reader.close()


os.rename( "D:\\files.txt","D:\\files2.txt" )
os.remove("D:\\files2.txt")
os.rmdir('dirname')
os.getcwd()
os.chdir("newdir")

