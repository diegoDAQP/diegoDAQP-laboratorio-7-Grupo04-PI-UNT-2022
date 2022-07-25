numb_list=[]

try:
  num=int(input('Ingrese la cantidad de valores: '))
except ValueError:
  print('El valor no es entero')
  
for x in range(num):
  numb_list.append([0]*1) #CREACIÓN DE LA MATRIZ
for numero in range(num):
  numb_list[numero] = int(input(f'Ingrese el {numero+1}° número entero: ')) 
try:
  n=int(input('Ingrese el entero objetivo: '))
  object=n
except ValueError:
  print('El valor no es entero')

def suma_obj(numb_list,object):  
  for first in range(len(numb_list)):
    for second in range(len(numb_list)):
      if numb_list[first] != numb_list[second] :   
        if object == numb_list[first] + numb_list[second] : 
          print(f'[{first} , {second}]')
          exit()       
print(suma_obj(numb_list,object))