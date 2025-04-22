# Función normal
def multiplicar_por_dos(numero):
    return numero*2

print(multiplicar_por_dos(5)) # 10

#nombre de funcion = lambda parm: expresion
multiplicar_por_dos = lambda  x:  x * 2

print(multiplicar_por_dos(5))

#Beneficios
    #Podemos utilizarlo para algo sencillo y rápido
    #Regresan un valor automáticamento (no tenemos que agregar un return)
#Desventajas
    #No son aptas para más de una instrucción
    
#########################################################
#########################################################

# Números pares

def es_par(numero):
    if(numero % 2 == 0):
        return True

numeros = [1,2,3,4,5,6,7,8,9]

#Usando filter con una función común
numeros_pares = filter(es_par,numeros)

#Regresa solo los pares
print(list(numeros_pares))


# Con lambda lo hacemos en una sola linea
numeros_pares = filter(lambda num: num % 2 == 0,numeros)
print(list(numeros_pares))
