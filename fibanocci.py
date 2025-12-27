def fibonocci(n):
    if n<=1:
        return n
    return fibonocci(n-1)+fibonocci(n-2)
print(fibonocci(7))
