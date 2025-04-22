import csv

with open("9_Archivos\\archivo_csv.csv") as archivo:
    #Retorna un iterable
    reader = csv.reader(archivo)
    for row in reader:
        print(row)

################################################################################################
################################################################################################
        
#Data frame es una estructura de dato bidimencional similar a una tabla de excel
import pandas as pd

df_archivo  = pd.read_csv("9_Archivos\\archivo_csv.csv", names=['nombre','apellido','edad'], skiprows=[0])
print(df_archivo.head())

# reordenar columnas
print(df_archivo['edad'].head())

# reordenar por edad
print(df_archivo.sort_values(by='edad',ascending= True))

#concatenar df
print(pd.concat([df_archivo,df_archivo]))

print("#################################")
#Primeras 3
print(df_archivo.head(3))
#Ultimas 3
print(df_archivo.tail(3))
print("#################################")

filas, columnas = df_archivo.shape

#Analisis estadistico
print(df_archivo.describe())

################################################################################################
################################################################################################


#Accediendo a un elemento específico con loc
#Accediendo a la edad de la fila 2 con loc
#                          fila, columna
elemento_df = df_archivo.loc[2,'edad']
print(elemento_df)

#Accediendo a la edad de la fila 2 con iloc 
#                indice de fila, columna
elemento_df = df_archivo.iloc[2,2]
print(elemento_df)
 

# Accediendo a todos los valores de una columna con loc
columna_df = df_archivo.loc[:,'nombre']
print(columna_df)

# Accediendo a todos los valores de una columna con iloc
columna_df = df_archivo.iloc[:,1]
print(columna_df)


# Accediendo a todos los valores de una columna con loc
fila_df = df_archivo.loc[2,:]
print(fila_df)

# Accediendo a todos los valores de una columna con iloc
fila_df = df_archivo.iloc[2,:]
print(fila_df)

mayor_que_20 = df_archivo.loc[df_archivo['edad']>20,:]
print(mayor_que_20)

#Slicing
cadena = "abcdefghijklmnopqrstuvwxyz"

print(cadena[0:10])
print(cadena[3:10])

################################################################################################
################################################################################################


# Para archivos grandes utilizar
import pandas as pd
def read_csv_in_chuncks(file_name):
    for i, chunk in enumerate(pd.read_csv(file_name,chunksize=1000)):
        print("chunk #{}".format(i))
        print(chunk)

read_csv_in_chuncks("9_Archivos\\big_file.csv")