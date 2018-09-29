def chocolateFeast(n, c, m):
    netChoc=n//c
    leftWrapper=netChoc

    while(leftWrapper>=m):
        newChoc=leftWrapper//m
        netChoc+=newChoc
        leftWrapper=leftWrapper%m
        leftWrapper+=newChoc
    return netChoc


print(chocolateFeast(15, 3, 2))
