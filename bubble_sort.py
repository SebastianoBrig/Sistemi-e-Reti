arr = []
n = input("inserisci la lunghezza: ")
for i in range(0, int (n)):
    valore = input("inserisci un valore: ")
    arr.append(int (valore))
for k in range (0, int (n)-1):
    for j in range (0, int (n)-k-1):
        if arr[j] > arr[j+1] : 
            arr[j], arr[j+1] = arr[j+1], arr[j] 
print(arr)