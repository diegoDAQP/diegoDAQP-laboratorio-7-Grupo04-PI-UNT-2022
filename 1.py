

def crear_matriz(a,b):  #definimos una función que cree matrices en forma de lista de listas
    matriz=[]  #definimos lo que será la matriz
       
    for i in range(a):   #bucle que establece el numero de filas
       
        fila=[] #definimos una fila cualquiera dentro del bucle para que se reinicie
        
        for j in range(b):   #bucle que establece el numero de columnas
            
            fila.append(int(input("Ingrese el elemento {}{} de la matriz: ".format(i+1,j+1))))    #agregamos un elemento a cada una de las filas
        
        matriz.append(fila)   #asignamos la fila creada a la matriz
        
    
    for i in range(a): #imprimimos la matriz 
        print(matriz[i])           
    return matriz    #la función devuelve la matriz que necesitamos

def mul_matr(m1,m2):
    
    m3 = []  #definimos la matriz 3 como la resultante de la multiplicación
    
    for i in range(len(m1)):   #bucle que hace un número de recorridos igual al número de filas de la matriz 1
        
        fila=[]   #definimos la lista que será cada una de las filas en esta posición para que se reinicie
        
        for k in range(len(m2[0])):   #bucle que hace un número de recorridos igual al número de columnas de la matriz 2
            
            element=0  #definimos cada elemento de la fila aquí para que se reincie
            
            for j in range(len(m2)):  #bucle que hace un número de recorridos igual al número de columnas de la matriz 2 (o columnas de la matriz 1)
            
                element+=m1[i][j]*m2[j][k]   #obtenemos cada elemento de la matriz resultante haciendo sumas
            
            fila.append(element)  #agregamos cada elemento a la fila
        
        m3.append(fila)     #agregamos cada fila a la matriz resultante
        
        for i in range(len(m3)):
            print(m3[i])
            
    return m3        
    
            


while True: 
    m = int(input("Escriba el número de filas de la primnera matriz: "))
    n= int(input("Escriba el número de columnas e la primera matriz: "))

    n2= int(input("Escriba el número de filas de la segunda matriz: "))
    p= int(input("Escriba el número de columnas e la segunda matriz: "))
    
    if n!=n2:
        print("Valores ingresados incorrectamente, recuerda que para multiplicar 2 matrices el número de columnas de la primera debe coincidir con el número de filas de la segunda")
        continue
    
    print("PARA LA PRIMERA MATRIZ")
    matriz_1=crear_matriz(m,n)
    
    print("PARA LA SEGUNDA MATRIZ")
    matriz_2=crear_matriz(n2,p)
        
    if n==n2: 
        print("EL RESULTADO DE LA MULTIPLICACIÓN ES: ")
        resultado = mul_matr(matriz_1,matriz_2)
        
        break
     
            
            
        
        
    