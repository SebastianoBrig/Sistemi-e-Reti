def fibonacci(n):
    n1=1
    n2=1
    for _ in range(n):
        print(n1, end=' ')
        n1,n2=n2,n1+n2
        print()
n = int(input("Inserisci il numero dei numeri totali:  "))
fibonacci(n)

