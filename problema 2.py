lista1=("M","C","X","I")
lista2=("R","D","L","V")
print("Ingrese el numero para realizar la conversion")
numero=int(input())
num=[]
num.append(numero//1000)
num.append(numero//100-((numero//1000)*10))
num.append(numero//10-((numero//100)*10))
num.append(numero-((numero//10)*10))
print("Numero arábigo: {}{}{}{}".format(num[0],num[1],num[2],num[3]))
if numero<4000 and numero>0:
    romano=[]
    i=0
    for i in range(4):
        if num[i]==9:
            romano.append(lista1[i]+lista1[i-1])
        elif num[i]<=8 and 5<num[i]:
            romano.append((lista2[i])+(lista1[i]*(num[i]-5)))
        elif num[i]==5:
            romano.append(lista2[i])
        elif num[i]==4:
            romano.append(lista1[i]+lista2[i])
        elif num[i]<=3 and 0<num[i]:
            romano.append(lista1[i]*(num[i]))
        elif num[i]==0:
            romano.append("")
        else:
            print("El numero es invalido")
else:
    print("El numero es invalido")
print("Numero Romano: {}{}{}{}".format(romano[0],romano[1],romano[2],romano[3]))