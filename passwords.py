import random
dizionario = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:"q", 11: "w", 12:"e", 13:"r", 14:"t", 15:"y", 16:"u", 17:"i", 18:"o", 19:"p",
20:"a", 21:"s", 22:"d", 23:"f", 24:"g", 25:"h", 26:"j", 27:"k", 28:"l", 29:"z", 30:"x", 31:"c", 32:"v", 33:"b", 34:"n", 35:"m", 36:"Q", 37:"W", 
38:"E", 39:"R", 40:"T", 41:"Y", 42:"U", 43:"I", 44:"O", 45:"P", 46:"A", 47:"S", 48:"D", 49:"F", 50:"G", 51:"H", 52:"J", 53:"K", 54:"L", 55:"Z", 
56:"X", 57:"C", 58:"V", 59:"B", 60:"N", 61:"M", 62:"_", 63:".", 64:"!", 67:"?", 68:"-"} 
password = []
def gen_pass(c):
    if int(c) == 1:
        for _ in range (8):
             n=random.randint(0,35)
             password.append(dizionario[n])
        print(password)
    else:
        for _ in range (20):
             n=random.randint(0,68)
             password.append(dizionario[n])
        print(password)
c=input("premi 1 per una password semplice oppure premi 2 per una password complicata: ")
gen_pass(c)
