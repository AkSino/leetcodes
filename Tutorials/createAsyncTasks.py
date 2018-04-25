from multiprocessing import Pool

def f(x):
    return x*x

def vardan():
    print("cmekmcwke")
pool=Pool(processes=1)
result=pool.apply(f,[10],vardan())