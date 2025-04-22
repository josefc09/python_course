# un evento es cualquier cosa que sucede en nuestro programa (click, notificación, movel el raton, tecla, etc.)
# una excepcion es algo que interrumpe el programa y donde nosotros tenemos que hacer algo

"""def suma():
    while True:
        num1 = input("Numero 1: ")
        num2 = input("Numero 2: ")
        try:
            resultado = int(num1) + int(num2)
        except:
            print("ambos valores deben ser númericos")
            # Podemos enviar como mensaje el error que lanza python
            print(f"ERROR: {e}")
            # Obteber el nombre de la excepción y agregarla al try (tomar en cuenta que si except general está en el try los demás no se ejecutan)
            print(f"Nombre del error: {type(e).__name__}")
        else:
            # Si todo sale bien, terminamos el bucle
            break
        finally:
            # Esto se ejecuta cada iteración casi no se utiliza 
            print("programa terminado")
    return resultado

print(suma())"""

#Podemos guardar tambien las excepciones

def suma():
    while True:
        num1 = input("Numero 1: ")
        num2 = input("Numero 2: ")
        try:
            resultado = int(num1) + int(num2)
        except ZeroDivisionError as e:
            print(f"No dividas por cero")
        except ValueError as ex:
            print(f"Agrega solo números")
        else:
            break
        finally:
            # Esto se ejecuta cada iteración casi no se utiliza 
            print("programa terminado")
    return resultado

print(suma())