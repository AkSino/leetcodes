#http://practice.geeksforgeeks.org/problems/start-elements/0
# code
# **is max (if unique)
# *is max(arr[a:])

def get_stars(arr):
    stars = []
    the_max = None
    dupe_max = True
    for item in reversed(arr):
        if the_max is None:
            the_max = item
            stars.append(the_max)
            dupe_max = False
        elif item > the_max:
            the_max = item
            stars.append(the_max)
            dupe_max = False
        elif item == the_max:
            dupe_max = True
    if dupe_max:
        the_max = -1
    return stars, the_max



arr=[4,2,5,7,2,1]
stars, starstar = get_stars(arr)
print(" ".join(str(x) for x in reversed(stars)))
print(str(starstar))


