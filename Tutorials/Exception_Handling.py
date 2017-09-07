#Various keywords associated with Exception Handling

try:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass

#Coding Begins
#First Scenario is that if there is some syntax error or any other error like file not found exception
try:
    f=open("svardan.txt")
except Exception:
    print ("Error in opening file. File does not exist")

#Problem with above code is that even if there is some other error apart from file not found in the try block, even then it
#will throw same error of Error in opening file. To overcome this we want to be precise with what our exception is.
# Code goes like this

try:
    f=open("vardan.txt")
    var=string_without_quote
except FileNotFoundError:
    print("Error in opening file")
#Above will be pronted only if there is some error in opening the file, else the regular exception willbe printed


#2- We can add multiple except also as below, In this case if Filenotfound then first error otherwise second one
except Exception:
    print("Some error occured")


#3- To print only the exception that the code threw and not the custom message we can use alias
try:
    f=open("vardan.txt")
    var=string_without_quote
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

#4- Else statement is used when we want to execute some code when there is no error in the try block
try:
    f=open("vardan.txt")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
#Upon running the above code contents of file will be printed.


#5- Finally will be executed no matter if any error is encountered in try or not.
try:
    f=open("vardan.txt")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("It will be executed finally")

#6- We can also raise manual exception if we want that certain condition should fall under exception.
#In below case else statement will not be executed. It is because file name will be considered as an manual exception by user.
try:
    f=open("vardan.txt")
    if f.name=="vardan.txt":
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("rkjvk")
else:
    print(f.read())
    f.close()
