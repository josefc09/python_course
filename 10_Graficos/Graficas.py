import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("datos_graficos.csv",names=["fecha","pasajeros"])


#           Tiene que tener el mismo nombre en el df
sns.lineplot(x="fecha", y="pasajeros", data=df)


# Encontrar el índice del máximo valor en la columna 'pds'
indice_maximo = df['pasajeros'].idxmax()

# Obtener las coordenadas del punto máximo
x_maximo = df.loc[indice_maximo, 'fecha']
y_maximo = df.loc[indice_maximo, 'pasajeros']

# Resaltar el punto máximo en el gráfico
plt.scatter(x_maximo, y_maximo, color='red', label='Máximo')

# Mostrar la leyenda
plt.legend()



plt.show()

