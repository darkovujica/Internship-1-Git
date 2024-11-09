def printanje(a,n):
    w = (n-len(a))//2
    print(" "*w + a + " "*w)
    
m = int(input())
n = int(input())
t = input()

l = t.split()
a = ""

for x in l:
    if len(a)+len(x)<=m:
        a=a+x+" "
    else:
        printanje(a[:-1],n)
        a=x+" "

printanje(a[:-1],n)

