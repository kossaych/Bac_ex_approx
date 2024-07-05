from django.shortcuts import render ,HttpResponse
def estpremier(x) :
    i = 2
    test = True
    while(test == True and i<= x//2) :
        if x%2 == 0 :
            test = False
        i = i + 1
    return test
def premier_suivant(n): 
    n += 1
    while not estpremier(n):
        n += 1
    return n
def Facteur(M) : 
    ch = ""
    while M > 1:
        i = 2
        while M % i != 0:
            i = premier_suivant(i)
        ch = ch  + str(i)
        M = M // i
    max = int(ch[0])
    for i in range (0,len(ch)) :
        if int(ch[i]) > max :
            max = int(ch[i])
    return max
def suitex(M,n,k) :
    if k == 0 :
        return M/2
    else :
        Tp = suitex(M,n,k-1)
        return (1 / n) * ((n - 1) * Tp + (M / (Tp ** (n - 1)))) 
def suitex0(M, n, k):
    if k == 0:
        return M / 2.0   
    else:
        Tp = suitex(M, n, k - 1)
        return (1 / n) * ((n - 1) * Tp + (M / (Tp ** (n - 1)))) 
def RacineN(M,n) :
    Tp = suitex(M,n,1)
    T = suitex(M,n,2)
    k = 2
    while(abs(Tp - T) > 0.0000000000000000000000000001) :
        Tp = T
        k = k + 1
        T = suitex(M,n,k)  
    return T
 
    
# Create your views here.
def home(request,id) : 
    M = int(id) 
    res = []
 
    n = 2
    p = Facteur(M)
    while(p < RacineN(M,n) ) :  
        res.append({'n' : n,'racine' : RacineN(M,n),'mark' : '<'}) 
        n = n+1 
    res.append({'n' : n,'racine' : RacineN(M,n),'mark' : '>'})
    print(res)
    return render(request,'home.html',{'M' : M ,'results' : res})