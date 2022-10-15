n = int(input("Digite o numero : "))
n1 = 1
n2 = 1
for count in range(2,n):
    n3 = n2+n1
    n2 = n1
    n1 = n3
    count += 1
print(n3)
aux = str(n3)
print(aux[-2], aux[-1])
