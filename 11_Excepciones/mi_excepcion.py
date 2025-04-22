class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Cometiste el siguiente error: {err}")
        

# raise sirve para lanzar excepciones
try:
    raise MiExcepcion("Prueba de error de excepcion")
except:
    print("No te vuelvas a equivocar mano")