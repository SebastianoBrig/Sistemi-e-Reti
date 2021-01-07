dizionario = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k", 11:"l", 12:"m", 13:"n", 14:"o", 
15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u", 21:"v", 22:"w", 23:"x", 24:"y", 25:"z"}
code = []
def get_key(val): 
    for key,value in dizionario.items():
        if val==value:
            return key

def codifica(code,n):
    for k in range (0,n):
        val=code[k]
        chiave=get_key(val)
        if chiave>10:
            chiave=chiave-26
        code[k]=dizionario[chiave+15]
    print(code)

def decodifica(code,n):
    for k in range (0,n):
        val=code[k]
        chiave=get_key(val)
        if chiave<15:
            chiave=chiave+26
        code[k]=dizionario[chiave-15]
    print(code)
    
c = int(input("inserisci 1 per effettuare la codifica oppure inserisci 2 per effettuare la decodifica: "))
n = int(input("inserisci la lunghezza della stringa: "))
print("inserisci i caratteri uno per volta")
for i in range (0,n):
    char=input()
    code.append(char)
if c==1:
    codifica(code,n)
else:
    decodifica(code,n)
