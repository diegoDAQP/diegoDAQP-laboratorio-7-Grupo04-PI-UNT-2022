def es_capicua(num):

   num = num.lower()

   num = num.replace(' ', ' ')

   long = len(num)
   
   if long % 2 == 0:
     izquierda = num[: long // 2]
     derecha = num[long // 2:]
   else:
        izquierda = num[:long // 2]
        derecha = num[long // 2+1:]
        
 
   return izquierda == derecha [::-1]
   
print(es_capicua(input("Escriba el número natural a analizar: ")))