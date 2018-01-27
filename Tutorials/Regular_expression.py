import re
a='''
vardan 
vardaan.gupta27@gmail.co.in
'''
#In compile method me define our regular expression
extract=re.compile(r'[a-z._A-Z0-9][a-z0-9]*@[a-zA-Z0-9]*\.[a-z.]*')
#In finditer method we define the string on which we have to run our regular expression
arr=extract.finditer(a)

for each in arr:
    #Prints the
    print(each)
    #Prints the span of found pattern
    p=(each.span()[1])
    q = (each.span()[0])

a='''
hh vardan
'''
#In compile method me define our regular expression
extract=re.compile(r'a')

#In finditer method we define the string on which we have to run our regular expression
arr=extract.finditer(a)

for each in arr:
    #Prints the
    print(each)
    #Prints the span of found pattern
    p=(each.span()[1])
    q = (each.span()[0])