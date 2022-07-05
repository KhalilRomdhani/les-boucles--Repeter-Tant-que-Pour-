def lire():
    global n
    while True :
        n=int(input("n="))
        if n>=10 :
            break
def pour(n):
    global R
    R=0
    for i in range(1,n):
        R=i*i
    return R
def repeter(n):
    global E
    E=0
    i=1
    while True :
        E=i*i
        print(E)
        i=i+1
        if i>=10 :
            break
def kenhakaraw(R,E):
    if R==E :
        print("le boucle pour",R,"est agule le boucle",E)
    else :
        print("le boucle pour",R,"n'est agule pas le boucle",E)
#Programe Principale
lire()
pour(n)
repeter(n)
kenhakaraw(R,E)