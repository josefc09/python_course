"""
lista([var,...,var]) Crea una lista
len(lista) Cuenta la cantidad de elementos
lista.append(valor) Agrega un elemento
lista.insert(ind,valor)  Agrega un elemento en un indice especificado
lista.extend([valor1,..., valorN]) Agrega varios elementos 
lista.pop(indice) Eliminando un elemento por indice
lista.remove("") Eliminando un elmento por su valor 
lista.sort() Ordena números y boleanos de manera ascendente
lista.sort(reverse = True) Ordena números y boleanos de manera descendente
lista.reverse() Invierte el orden de la lista [1,2,3,4] = [4,3,2,1]
lista.clear() Elimina todos los elementos
"""

lista = list(["Hola", 1 ,True])
print(lista)
print(len(lista))

lista.append("bien")
print(lista)

lista.insert(3, "mal")
print(lista)

lista.extend([True, 5])
print(lista)

lista.pop(0)
print(lista)

lista.remove("mal")
print(lista)

lista = list([95,25,33,74,True, False])
lista.sort()
print(lista)
lista.sort(reverse= True)
print(lista)

lista = list([95,25,33,74,True, False])
lista.reverse()
print(lista)

lista.clear()
print(lista)