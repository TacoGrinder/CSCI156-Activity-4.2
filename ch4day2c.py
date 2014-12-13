__author__ = 'Sean'


def less(n):
    s = str(n-1)
    for i in reversed(range(1, n-1)):
        s=s+","+str(i)
    return(s)

def descend(x):
    s = ""
    for i in range(1, x+1):
        s=s+str(i)+". "+less(i+1) + "\n"
    print(s)


descend(5)