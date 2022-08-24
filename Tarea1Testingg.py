def factor_genero(genero):
    if genero.upper() == 'M':
        factorG =0.6176118
    elif genero.upper() =='F':
        factorG = 0
    return factorG

    
def factor_edad(edad):
    
        if edad < 20:
            factor = 0
        elif edad >= 20 and edad < 30:
            factor = -1.458102
        elif edad >= 30 and edad < 40:
            factor = -1.196494
        elif edad >= 40 and edad < 50:
            factor = -0.9109254
        elif edad >= 50 and edad < 60:
            factor = 1.888158
        elif edad >= 60 and edad < 70:
            factor = 2.93897
        elif edad >= 70 and edad < 80:
            factor = 3.774616
        elif edad >= 80:
            factor = 4.456995
        
        return factor
    
def factor_comorbilidad(Palabra):
  
    Enfermedad = []
    Suma = 0
    
    for num in palabra:
        if num not in Enfermedad:
            Enfermedad.append(num)

    for a in Enfermedad: 
        if a == '1':
            Suma+= 2.003496
        elif a == '2':
            Suma+= 2.21035
        elif a == '3':
            Suma+= 2.550317
        elif a == '4':
            Suma+= 2.036501
        elif a == '5':
            Suma+= 1.925291
            

    return Suma
        
        
print("***********Calculadora de la muerte ***********\n")

while True:
    print("---------------------------------")
    print("Ingrese nombre: ")
    nombre = str(input())

    while(True):
        print("1. Ingresar edad: ")
        edad = int(input("Ingrese su edad: "))
        if edad > 120:
            print ("No puede ingresar una edad mayor o igual a 120, intente nuevamente")
        elif edad < 0:
            print("No puede ingresar una edad negativa, intente nuevamente")
        else:
            break

    print("2. Ingresar genero: 'M' o 'F'" )
    genero= str(input())
    factor_Edad = factor_edad(edad)
    factor_Genero = factor_genero(genero)
    
    print("Menu de opciones \n")
    print("1. Tiene una de estas enfermedades: (Hipertenso, Diabetes, Enfermedad Cardiaca, Enfermedad respiratoria, Cancer)")
    print("2. Otra (Ingrese cual): ")
    print("3. Ninguna enfermedad\n")
    print("Ingrese opcion: ")
    opcion = int(input())
    
    if opcion == 1:
        print("Listado de enfermedades\n")
        print("1. Hipertenso")
        print("2. Diabetes")
        print("3. Enfermedad cardiaca")
        print("4. Enfermedad respiratoria")
        print("5. Cancer")
        print("Ingrese tipo de enfermedades(Si es más de una poner numero seguidos Ej: 123)")    
   
        palabra = str(input())     
        factor_Comorbilidad = factor_comorbilidad(palabra) 
        
        break
    
    if opcion == 2:
        print("Ingrese enfermedad que tiene: ")
        
        break
        
    if opcion == 3:
        print("No tiene enfermedad, por lo tanto su valor de comorbilidad es 0")
        
        break
    break
         
factor_Edad = factor_edad(edad)
factor_Genero = factor_genero(genero) 
factor_Comorbilidad = factor_comorbilidad(palabra)  
constante = -7.547078
e = 2.71828

print("Hola", nombre)
print("Tiene una comorbilidad de: " ,factor_comorbilidad(palabra))
Riesgo = constante + factor_edad(edad) + factor_genero(genero) + factor_comorbilidad(palabra)
print("su riesgo de muerte es: ",Riesgo)

Prob_fallecer = (e**Riesgo)/(1+e**Riesgo)
print("Y su probabilidad de fallecimiento debido al covid es: ", Prob_fallecer)

        
    
    
    




    
    