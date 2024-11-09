def perm(a,n):
    if n==0:
        #print(a)
        
        s = ""
        for x in a:
            s+= str(x) + " "
        print(s[:-1])
        
        
    else:
        for i in range(n):
            perm(a[:i]+a[i+1:]+[a[i]],n-1)
        

lista = list(map(int, input().split()))
perm(lista,len(lista))
