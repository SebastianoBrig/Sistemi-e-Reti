dizionario = {}
def max_min(anno_1,anno_2):
    max = -1000
    min = 1000
    while anno_1<=anno_2:
        if dizionario[anno_1]>max:
            max = dizionario[anno_1]
        if dizionario[anno_1]<min:
            min = dizionario[anno_1]
        anno_1=anno_1+1
    print("il valore massimo e':", max ,"il valore minimo e':", min)
def lettura(file):
    k=1
    p=1
    for riga in file:
        if p==0:
            if k==1:
                line = riga.split(',')
                chiave = int(line[1])
                val1 = float(line[2])
                k=2
            else:
                line = riga.split(',')
                val2 = float(line[2])
                media=(val1+val2)/2
                dizionario[chiave]=media
                k=1
        else:
            p=0
file = open("./annual.csv", "r")
lettura(file)
anno_1 = int(input("inserisci l'anno 1: "))
anno_2 = int(input("inserisci l'anno 2: "))
max_min(anno_1,anno_2)       
            

