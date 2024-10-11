"""
-----------------------------------------------------------------------------------------------
Título: Cinema
Fecha: 14 de octubre del 2024 
Autor:

Descripción:

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def crear_sala(sala_usuario, filas, columnas):
    salon = []
    for _ in range(filas):
        # Cada fila es un diccionario donde la clave es el número de columna y el valor es "empty"
        fila = {columna: "empty" for columna in range(columnas)}
        salon.append(fila)
    return salon


def agregar_pelicula(peliculas):
    nombre_pelicula = input("Ingrese el nombre de la película: ")
    duracion = input("Ingrese la duración de la película (ej. 120 minutos): ")
    genero = input("Ingrese el género de la película: ")
    
    # Se agrega la película como una entrada al diccionario
    peliculas[nombre_pelicula] = {"duracion": duracion, "genero": genero}
    
    print("*********")
    print(f"LA PELICULA ''{nombre_pelicula}'' FUE AGREGADA A LA LISTA EXITOSAMENTE :) !")
    print("*********")

def borrar_pelicula(peliculas):
    nombre_pelicula_borrar = input("Ingrese el nombre de la pelicula que quiera borrar: ")
    
    if nombre_pelicula_borrar in peliculas:
        del peliculas[nombre_pelicula_borrar]
        print(f"La pelicula", {nombre_pelicula_borrar} ,"se borro con exito")
    else:
        print("La pelicula no existe")

def mostrar_peliculas(peliculas):
    if peliculas:
        print("Películas Disponibles:")
        print()
        for nombre_pelicula, detalles in peliculas.items():
            print(f" {nombre_pelicula} (Duracion: {detalles['duracion']}, Genero: {detalles['genero']})")
    else:
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("NO HAY PELICULAS DISPONIBLES")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def dibujar_salon(salon, sala_usuario, filas, columnas):
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w"]
    
    # Imprimir la parte superior del salón
    print("" + "" * (columnas*3) + "_")
    print("|"+ " " * int(columnas // 2), "    {Pantalla}", " " * (columnas//2)+ "       |")
    
    # Imprimir los números de las columnas
    numero_columnas = "|    " + " ".join([str(i+1) for i in range(columnas)])+ ""
    print(f"{numero_columnas}  |")
    
    # Imprimir las filas del salón
    for idx, fila in enumerate(salon):
        printeame = ""
        for columna in fila:
            estado = fila[columna]
            printeame += " O" if estado == "empty" else " X"
        print(f"| {abecedario[idx]} {printeame}      |")
    
    # Imprimir el soporte base
    print("|" + "" * (columnas*2)+ "__|")

def reservar_asiento(salon, seleccion, nombre):
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w"]
    letra = ""
    numeros = ""
    for char in seleccion:
        if char.isalpha():  # Si es letra
            letra += char
        elif char.isdigit():  # Si es número
            numeros += char

            
    bandera = 0
    for i in abecedario:
        contador = 0
        if i == letra:
            fila = salon[contador]
            if fila[int(numeros)-1] == "empty":
                fila[int(numeros)-1] = nombre
                print("Reservado exitosamente!")
                print(salon)
                bandera += 1 
                return salon
            elif fila[int(numeros)-1] != "empty":
                return print("Perdon aun no pense esta solucion de manera correcta")
        else:
            contador += 1
            continue
    if bandera == 0: 
        print("Lo lamento, no fue posible reservar el asiento.")

def opcion_2(peliculas, salas_cine, salas_reservas):
    print("Selecciona la pelicula que quieras ver")
    print("Cartelera")
    print("------------------------------------------------------")
    print(('| ' + ' | '.join(peliculas.keys()) + ' |'))
    print("------------------------------------------------------")

    x = input("Escribe el nombre de la pelicula que quieras ver: ")

    
    if x in peliculas.keys():
            buscar_sala = peliculas[x]["proyectadaEn"]
            sala_seleccionada = salas_cine[buscar_sala]


            if x not in salas_reservas.keys():
                print("corriendo opcion1")
                salon = crear_sala(sala_seleccionada, sala_seleccionada["filas"], sala_seleccionada["columnas"])
                dibujar_salon(salon, sala_seleccionada, sala_seleccionada["filas"], sala_seleccionada["columnas"])

                seleccion = input("Selecciona el asiento que querés reservar: ")
                nombre = input("Su nombre por favor: ")
                salon = reservar_asiento(salon, seleccion, nombre)
                dibujar_salon(salon, sala_seleccionada, sala_seleccionada["filas"], sala_seleccionada["columnas"])
                print("Reserva realizada con éxito.")
                salas_reservas[x] = salon

            #JAAAAAAAAAAAAAAAAAAAA
            elif x in salas_reservas.keys():
                print("corriendo opcion2")
                dibujar_salon(salas_reservas[x], sala_seleccionada, sala_seleccionada["filas"], sala_seleccionada["columnas"])
                seleccion = input("Selecciona el asiento que querés reservar: ")
                nombre = input("Su nombre por favor: ")
                salas_reservas[x] = reservar_asiento(salas_reservas[x], seleccion, nombre)
                dibujar_salon(salas_reservas[x], sala_seleccionada, sala_seleccionada["filas"], sala_seleccionada["columnas"])

    else:
        print("Pelicula no encontrada. Por favor, intentar nuevamente.")
        opcion_2(peliculas,salas_cine)



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    salas_cine = {
        "sala1": {
            "tamaño": "chica",
            "filas": 9,
            "columnas": 6
        },
        "sala2": {
            "tamaño": "mediana",
            "filas": 17,
            "columnas": 13
        }
    }
    salas_reservas= {}
    # En este diccionario se agrega las peliculas que vayamos escribiendo
    peliculas = {
    "Avatar 2": {
        "proyectadaEn": "sala1",
        "descripcion": "?",
        "duracion": "120 minutos",
        "genero": "Ciencia ficción"
    },
    "Deadpool 3": {
        "proyectadaEn": "sala2",
        "descripcion": "?",
        "duracion": "115 minutos",
        "genero": "Acción/Comedia"
    }
}

    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        opciones = 4
        while True:
            print()
            print("---------------------------")
            print("BIENVENIDO A CINEMA           ")
            print("---------------------------")
            print("[1] Visualizar salon")
            print("[2] Reservar cine")
            print("[3] Agregar pelicula")
            print("[4] Mostrar peliculas")
            print("---------------------------")
            print("[0] Salir del programa")
            print()
            
            opcion = input("Seleccione una opcion: ")
            if opcion in ["0" ,"1" , "2" , "3" , "4"]:# Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcion == "1":   # Opción 1
            entrada_usuario = input("Selecciona tu sala (ej.: sala1): ")
            if entrada_usuario in salas_cine:
                sala_seleccionada = salas_cine[entrada_usuario]
                salon = crear_sala(sala_seleccionada, sala_seleccionada["filas"], sala_seleccionada["columnas"])
                dibujar_salon(salon, sala_seleccionada, sala_seleccionada["filas"], sala_seleccionada["columnas"])
            else:
                print("Sala no encontrada. Inténtalo de nuevo.")
        elif opcion == "2":   # Opción 2
            opcion_2(peliculas, salas_cine, salas_reservas)
        elif opcion == "3":   # Opción 3
            print()
            print("-------------------------------")
            print("SELECCIONE LO QUE QUIERE HACER")
            print("-------------------------------")
            print("[1] Agregar una pelicula")
            print("[2] Borrar una pelicula")
            print("-------------------------------")
            
            opcion_modulo3 = input("Seleccione una opcion: ")
            if opcion_modulo3 in ["1" , "2"]: # Sólo continua si se elije una opcion de menú válida
                if opcion_modulo3 == "1":
                    agregar_pelicula(peliculas)
                elif opcion_modulo3 == "2":
                    borrar_pelicula(peliculas)
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()
        
        elif opcion == "4":   # Opción 4
            mostrar_peliculas(peliculas)

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()