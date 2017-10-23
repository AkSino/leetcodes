#Its a tutorial for Python format characters

integer=23
character='v'
string=13
float=12.344

print ("My age is %d %d" %(integer,integer))
print("First letter is %c" %character)
print("My salary was %sk" %string)
print("My height is %f ft" %float)  #prints default float
print("My height is %.1f ft" %float)  #Prints float upto predefined decimal points
print(round(1.33))

print("%r" %character)


print ("pandas: {}".format(1.4))