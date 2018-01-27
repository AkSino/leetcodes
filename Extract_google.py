import re
arr='''
baby'''
#In compile method me define our regular expression
extract=re.compile(r'[a-z]*b')
#In finditer method we define the string on which we have to run our regular expression
ans=extract.finditer(arr)

for each in ans:
    #Prints the
    #Prints the span of found pattern
    p=(each.span()[1])
    q = (each.span()[0])
    print(arr[q:p])
