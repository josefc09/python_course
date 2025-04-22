# Funciones build in son funciones integradas son las funciones creadas por Python

lista_num = [21,12,43,2,34,5,6,7]

max_num = max(lista_num)
print(f"Número máximo: {max_num}")

min_num = min(lista_num)
print(f"Número mínimo: {min_num}")

print(f"Redondeando 12.323423 sin decimales= {round(12.323423)}")
print(f"Redondeando 12.323423 a dos decimales= {round(12.323423,2)}")

# Retorna False -> 0, vacio, False, None
# Retorna True -> True, cadena, float, int != 0 
print(f"Verificando 0: {bool(0)}")
print(f"Verificando vacio: {bool()}")
print(f"Verificando False: {bool(False)}")
print(f"Verificando None: {bool(None)}")

print(f"Verificando True: {bool(True)}")
print(f"Verificando cadena: {bool("ad")}")
print(f"Verificando 21.1: {bool(21.1)}")
print(f"Verificando -1: {bool(-1)}")

# Retorna False si hay un elemento -> 0, vacio, False, None, []
lista = ["hola", 0, True, [1,"gato"]]
print(f"Verificando datos en lista: {all(lista)}") # False porque hay un 0

suma_total = sum(lista_num)
print(f"Suma total {suma_total}")

#round(numero, ndigits=None): Redondea un número al número de dígitos especificado (o 0 si no se especifica).
numero_redondeado = round(3.14159, 2)
print(numero_redondeado)  # Output: 3.14

#Funciones para trabajar con booleanos:
#bool(valor): Convierte un valor a un booleano.
resultado_bool = bool(0)
print(resultado_bool)  # Output: False

#all(iterable): Retorna True si todos los elementos en el iterable son verdaderos.
lista_booleanos = [True, True, False, True]
resultado_all = all(lista_booleanos)
print(resultado_all)  # Output: False

#any(iterable): Retorna True si al menos un elemento en el iterable es verdadero.
lista_booleanos = [True, False, False, False]
resultado_any = any(lista_booleanos)
print(resultado_any)  # Output: True