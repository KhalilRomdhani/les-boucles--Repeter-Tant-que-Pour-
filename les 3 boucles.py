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
def tant_que():
    global Z
    i=1
    while i<10 :
        Z=i*i
        print(Z)
        i=i+1
def kenhakaraw(R,E,Z):
    if R==E==Z :
        print("le boucle pour",R,"est agule le boucle",E,"aussi le blocle tant que",Z)
    else :
        print("le boucle pour",R,"n'est agule pas le boucle",E,"aussi le blocle tant que",Z)
#Programe Principale
lire()
pour(n)
repeter(n)
tant_que()
kenhakaraw(R,E,Z)