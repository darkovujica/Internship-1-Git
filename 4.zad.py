n = int(input())
if n%2==1:
    a="*"
    for i in range(n//2):
        b = " "*(n//2-i)
        print(b+a+b)
        a+="**"
        
    print(a)
    
    for i in range(n//2):
        a = a[:-2]
        b = " "*(i+1)
        print(b+a+b)
        
