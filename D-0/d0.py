N =  int(input("Informe o tamanho do array: "))
aux=[]
for count in range(N):
    aux.append(count+1)
print(aux)

for i, v in enumerate(aux):
    if not i % 2:
        print(v)
        
#for count1 in range(N):
#    if count1 % 2 == 0:
#        print(aux[count1])
