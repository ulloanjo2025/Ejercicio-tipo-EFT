# Diccionarios entregados
alumnos = {
    '1-1': ['Susana', 19, 'F', 'susana@duocuc.cl'],
    '2-2': ['Juan', 22, 'M', 'juan@duocuc.cl'],
    '3-3': ['Carlos', 21, 'M', 'carlos@duocuc.cl'],
    '4-4': ['David', 25, 'M', 'david@duocuc.cl'],
    '5-5': ['Camila', 23, 'F', 'camila@duocuc.cl'],
    '6-6': ['Sandra', 21, 'F', 'sandra@duocuc.cl'],
    '7-7': ['Carmen', 23, 'F', 'carmen@duocuc.cl'],
    '8-8': ['Andrés', 21, 'M', 'andres@duocuc.cl'],
}

cursos = {
    '1-1': ['introducción a Python', 100000],
    '2-2': ['introducción a Python', 100000],
    '3-3': ['introducción a Python', 100000],
    '4-4': ['introducción a Python', 100000],
    '5-5': ['introducción a Python', 100000],
    '6-6': ['Python POO', 150000],
    '7-7': ['Python POO', 150000],
    '8-8': ['Python POO', 150000],
}

# Función para buscar alumno por RUT
def buscar_por_rut(rut):
    if rut in alumnos:
        nombre, edad, genero, correo = alumnos[rut]
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Género: {genero}")
        print(f"Correo: {correo}")
    else:
        print("El rut ingresado no existe.")

# Función para listar alumnos por edades
def busqueda_edades(edad_min, edad_max):
    lista_filtrada = []

    for rut, datos in alumnos.items():
        nombre, edad, genero, correo = datos
        if genero == 'F' and edad_min <= edad <= edad_max:
            curso = cursos[rut][0]
            lista_filtrada.append(f"{nombre}--{curso}")

    if lista_filtrada:
        for dato in sorted(lista_filtrada):
            print(dato)
    else:
        print("No hay alumnos en ese rango de edades.")

# Función para actualizar correo
def actualizar_correo(rut, correo):
    if rut in alumnos:
        alumnos[rut][3] = correo.lower()
        return True
    else:
        return False

# Menú principal
def main():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Datos de alumno.")
        print("2. Listar alumnos por edades.")
        print("3. Actualizar correo.")
        print("4. Salir.")

        opcion = input("Ingrese una opción: ")

        match opcion:
            case '1':
                rut = input("Ingrese el RUT del alumno: ")
                buscar_por_rut(rut)

            case '2':
                while True:
                    try:
                        edad_min = int(input("Ingrese edad mínima: "))
                        edad_max = int(input("Ingrese edad máxima: "))
                        break
                    except ValueError:
                        print("Debe ingresar valores enteros!!")
                busqueda_edades(edad_min, edad_max)

            case '3':
                while True:
                    rut = input("Ingrese el RUT del alumno: ")
                    nuevo_correo = input("Ingrese el nuevo correo: ")
                    resultado = actualizar_correo(rut, nuevo_correo)
                    if resultado:
                        print("Correo actualizado!!")
                    else:
                        print("El rut no existe!!")

                    continuar = input("¿Desea actualizar otro correo? (si/no): ").lower()
                    if continuar != 'si':
                        break

            case '4':
                print("Fin del Programa.")
                break

            case _:
                print("Opción no válida, intente nuevamente.")

# Ejecutar el programa
main()
