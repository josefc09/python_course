#Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_cursos = 1.5

# Duración de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duración
diferencia_con_min = 100 - (dalto_cursos / otros_cursos_min * 100)
diferencia_con_max = 100 - (dalto_cursos / otros_cursos_max * 100)
diferencia_con_promedio = 100 - (dalto_cursos / otros_cursos_promedio * 100)

#Calculando el porcentaje de tiempo removido
tiempo_vacio_promedio = 100 - (otros_cursos_promedio / crudo_promedio * 100)
tiempo_vacio_dalto = 100 - (dalto_cursos / crudo_dalto * 100)

#Ejercicio A
print("El curso de Dato dura: ")
print(f" - un {diferencia_con_min}% menos que el más rápido.")
print(f" - un {round(diferencia_con_max,1)}% menos que el más lento.")
print(f" - un {diferencia_con_promedio}% menos que el promedio.\n")

#Ejercicio B
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"Este curso eliminó el {round(tiempo_vacio_dalto,1)}% de tiempo vacio.\n")

#Mostrando diferencias si los cursos duraran 10 hrs.
print(f"Ver 10 horas de este curso equivale a ver {round(otros_cursos_promedio / dalto_cursos * 10,1)} horas de tiempo vacio.")
print(f"Ver 10 horas de otros curso equivale a ver {round(dalto_cursos / otros_cursos_promedio * 10,1)} horas de tiempo vacio.")