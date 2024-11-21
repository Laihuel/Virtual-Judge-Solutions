from io import open
from sys import stdin, stdout

estoyEnVsCode=True
if(estoyEnVsCode):
    stdin=open("C:/Users/ASUS/Desktop/Facultá 6to Semestre/Problemas/COLWORD/input.txt", "r")
    stdout=open("C:/Users/ASUS/Desktop/Facultá 6to Semestre/Problemas/COLWORD/output.txt", "w")

def preprocesamientoKMP(P):
    b=[0]*(len(P)+1)
    i=0
    j=-1
    b[0]=-1
    while (i < (len(P))):
        while (j >= 0 and P[i] != P[j]):
            j=b[j]
        i=i+1
        j=j+1
        b[i]=j
    return(b)

def busquedaKMP(T, P):
    b=preprocesamientoKMP(P)
    indices=[False]*len(T)
    i=0
    j=0
    while (i < len(T)):
        while (j >= 0 and T[i] != P[j]):
            j=b[j]
        i=i+1
        j=j+1
        if (j==len(P)):
            indices[i-j]=True
            j=b[j]
    return(indices)



#Cuerpo
MOD = 1000000007
cant = stdin.readline()
cantCasos=int(cant[0:(len(cant)-1)])


for i in range (0, cantCasos):
    N = stdin.readline()
    N=N[0:len(N)-1]
    largoN=len(N)
    W = stdin.readline()
    if (W[len(W)-1]=='\n'):
        W=W[0:len(W)-1]
    largoW=len(W)

    indices = busquedaKMP(N, W)
    dp=[0]*largoN
    if(indices[0]):
        dp[0]=1
    else:
        dp[0]=0
    for j in range (1, largoN):
        if indices[j]:
            if j >= largoW:
                dp[j]= (dp[j-1]+dp[j-largoW]+1)%MOD
            else:
                dp[j]= (dp[j-1]+1)%MOD
        else:
            dp[j]=(dp[j-1])%MOD
    stdout.write(str(dp[largoN-1]))
    stdout.write('\n')


        


