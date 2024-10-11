"""
-----------------------------------------------------------------------------------------------
Título: Cinema
Fecha: 14 de octubre del 2024 
Autores: Berrutto Walter, Nisi Giancarlo, Rojas Naomy, Miño Lautaro y Rudd Sorensen Joaquina.

Descripción: Este sistema de reservas para cine consiste en administrar todo lo requerido para la correcta gestión del lugar.
Por un lado, los usuarios pueden reservar fácilmente sus entradas eligiendo tanto la película como el asiento de su preferencia.
Al completar la reserva, recibirán un ticket con todos los detalles, incluyendo la sala donde se proyectará la película.
Por el otro, el sistema ofrece a los empleados del cine la flexibilidad de actualizar el catálogo de películas, asignar las salas para cada función y, cuando sea necesario, ajustar la estructura o capacidad de las mismas.


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
    nombre_pelicula_borrar = input("Ingrese el nombre de la pelicula que quiera borrar: ") #el usuario ingresa una pelicula que quiera borrar
    
    if nombre_pelicula_borrar in peliculas: #si la pelicula esta en el catalogo se borrará, sino se le informará que la pelicula no existe
        del peliculas[nombre_pelicula_borrar]
        print(f"La pelicula", {nombre_pelicula_borrar} ,"se borro con exito")
    else:
        print("La pelicula no existe")
        
def modificar_pelicula(peliculas):
    print("*********")
    print("Cartelera de cine actual") #enseña la cartelera actual del cine
    for nombre_pelicula in peliculas:
        print(nombre_pelicula)
    print("*********")
    
    pelicula_modificar = input("Ingrese el nombre de la pelicula que quiera modificar: ")
    
    if pelicula_modificar in peliculas: #si la pelicula escrita existe en la cartelera la modificará
        print("*********")
        print("[1] Modificar nombre de la pelicula")
        print("[2] Modificar duracion de la pelicula")
        print("[3] Modificar genero de la pelicula")
        print("*********")
        
        seleccion_modificar_pelicula = input("Ingrese lo que quiere modificar de la pelicula ")
        
        if seleccion_modificar_pelicula == "1": #modifica el nombre, la duracion y el genero de la pelicula
            nombre_nueva_pelicula = input("Ingrese el nuevo nombre de la pelicula")
            datos_pelicula = peliculas[pelicula_modificar]
            del peliculas[pelicula_modificar]
            peliculas[nombre_nueva_pelicula] = datos_pelicula
        elif seleccion_modificar_pelicula == "2":
            duracion_nueva_pelicula = input("Ingrese la nueva duracion de la pelicula")
            peliculas[pelicula_modificar]["duracion"] = duracion_nueva_pelicula
        elif seleccion_modificar_pelicula == "3":
            genero_nueva_pelicula = input("Ingrese el nuevo genero de la pelicula")
            peliculas[pelicula_modificar]["genero"] = genero_nueva_pelicula
        
    else:
        print("La pelicula que se quiere modificar no existe en el catalogo")
    

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
        "descripcion": "Una batalla épica por la supervivencia en Pandora.",
        "duracion": "120 minutos",
        "genero": "Ciencia ficción"
    },
    "Deadpool 3": {
        "proyectadaEn": "sala2",
        "descripcion": "El irreverente antihéroe regresa con más caos.",
        "duracion": "115 minutos",
        "genero": "Acción/Comedia"
    },
    "El Señor de los Anillos: La Comunidad del Anillo": {
        "proyectadaEn": "sala3",
        "descripcion": "Un grupo de héroes emprende una misión para destruir un anillo poderoso.",
        "duracion": "178 minutos",
        "genero": "Fantasía/Aventura"
    },
    "Interstellar": {
        "proyectadaEn": "sala4",
        "descripcion": "Astronautas viajan a través de un agujero de gusano en busca de un nuevo hogar para la humanidad.",
        "duracion": "169 minutos",
        "genero": "Ciencia ficción"
    },
    "El Padrino": {
        "proyectadaEn": "sala5",
        "descripcion": "La saga de una familia mafiosa en busca de poder y redención.",
        "duracion": "175 minutos",
        "genero": "Drama/Crimen"
    },
    "Matrix": {
        "proyectadaEn": "sala6",
        "descripcion": "Un programador descubre la aterradora verdad detrás de su realidad.",
        "duracion": "136 minutos",
        "genero": "Ciencia ficción/Acción"
    },
    "Jurassic Park": {
        "proyectadaEn": "sala7",
        "descripcion": "Dinosaurios clonados causan estragos en un parque temático.",
        "duracion": "127 minutos",
        "genero": "Aventura/Ciencia ficción"
    },
    "Titanic": {
        "proyectadaEn": "sala8",
        "descripcion": "Un romance florece a bordo del fatídico transatlántico.",
        "duracion": "195 minutos",
        "genero": "Drama/Romance"
    },
    "Gladiador": {
        "proyectadaEn": "sala9",
        "descripcion": "Un general romano busca venganza contra un emperador corrupto.",
        "duracion": "155 minutos",
        "genero": "Acción/Drama"
    },
    "Star Wars: El Imperio Contraataca": {
        "proyectadaEn": "sala10",
        "descripcion": "La rebelión lucha contra el poder del Imperio Galáctico.",
        "duracion": "124 minutos",
        "genero": "Ciencia ficción/Aventura"
    },
    "Los Vengadores: Endgame": {
        "proyectadaEn": "sala11",
        "descripcion": "Los héroes más poderosos de la Tierra enfrentan a Thanos en una batalla final.",
        "duracion": "181 minutos",
        "genero": "Acción/Ciencia ficción"
    },
    "Forrest Gump": {
        "proyectadaEn": "sala12",
        "descripcion": "La historia de un hombre cuyas acciones inocentes cambian el mundo.",
        "duracion": "142 minutos",
        "genero": "Drama/Comedia"
    },
    "El Rey León": {
        "proyectadaEn": "sala13",
        "descripcion": "Un joven león descubre su destino como rey de la sabana.",
        "duracion": "88 minutos",
        "genero": "Animación/Familia"
    },
    "Inception": {
        "proyectadaEn": "sala14",
        "descripcion": "Un ladrón de secretos a través de los sueños enfrenta su misión más compleja.",
        "duracion": "148 minutos",
        "genero": "Ciencia ficción/Acción"
    },
    "Toy Story": {
        "proyectadaEn": "sala15",
        "descripcion": "Los juguetes cobran vida cuando los humanos no están.",
        "duracion": "81 minutos",
        "genero": "Animación/Familia"
    },
    "The Dark Knight": {
        "proyectadaEn": "sala16",
        "descripcion": "Batman enfrenta a su peor enemigo: el Joker.",
        "duracion": "152 minutos",
        "genero": "Acción/Crimen"
    },
    "Pulp Fiction": {
        "proyectadaEn": "sala17",
        "descripcion": "Historias entrelazadas de crimen y redención en Los Ángeles.",
        "duracion": "154 minutos",
        "genero": "Crimen/Drama"
    },
    "Coco": {
        "proyectadaEn": "sala18",
        "descripcion": "Un joven músico viaja al mundo de los muertos para descubrir su herencia familiar.",
        "duracion": "105 minutos",
        "genero": "Animación/Familia"
    },
    "Mad Max: Furia en el Camino": {
        "proyectadaEn": "sala19",
        "descripcion": "En un futuro apocalíptico, un guerrero solitario busca redención.",
        "duracion": "120 minutos",
        "genero": "Acción/Aventura"
    },
    "La La Land": {
        "proyectadaEn": "sala20",
        "descripcion": "Un romance florece entre un músico y una actriz en Los Ángeles.",
        "duracion": "128 minutos",
        "genero": "Musical/Romance"
    },
    "Guardianes de la Galaxia": {
        "proyectadaEn": "sala21",
        "descripcion": "Un grupo de inadaptados se une para salvar el universo.",
        "duracion": "121 minutos",
        "genero": "Acción/Ciencia ficción"
    },
    "Shrek": {
        "proyectadaEn": "sala22",
        "descripcion": "Un ogro gruñón embarca en una misión para rescatar a una princesa.",
        "duracion": "90 minutos",
        "genero": "Animación/Comedia"
    },
    "Rocky": {
        "proyectadaEn": "sala23",
        "descripcion": "Un boxeador aficionado tiene una oportunidad de luchar por el título mundial.",
        "duracion": "120 minutos",
        "genero": "Drama/Deportes"
    },
    "Harry Potter y la Piedra Filosofal": {
        "proyectadaEn": "sala24",
        "descripcion": "Un niño descubre que es un mago y comienza su educación en Hogwarts.",
        "duracion": "152 minutos",
        "genero": "Fantasía/Aventura"
    },
    "El Gran Showman": {
        "proyectadaEn": "sala25",
        "descripcion": "La historia del ascenso de P.T. Barnum y el circo que lo hizo famoso.",
        "duracion": "105 minutos",
        "genero": "Musical/Drama"
    },
    "Tiburón": {
        "proyectadaEn": "sala26",
        "descripcion": "Un gran tiburón blanco aterroriza una pequeña ciudad costera.",
        "duracion": "124 minutos",
        "genero": "Suspenso/Terror"
    },
    "Amélie": {
        "proyectadaEn": "sala27",
        "descripcion": "Una joven soñadora decide cambiar la vida de quienes la rodean.",
        "duracion": "122 minutos",
        "genero": "Comedia/Drama"
    },
    "Indiana Jones y los Cazadores del Arca Perdida": {
        "proyectadaEn": "sala28",
        "descripcion": "Un arqueólogo aventurero busca una reliquia sagrada.",
        "duracion": "115 minutos",
        "genero": "Aventura/Acción"
    },
    "Piratas del Caribe: La Maldición del Perla Negra": {
        "proyectadaEn": "sala29",
        "descripcion": "Un pirata excéntrico une fuerzas para recuperar su barco y luchar contra una tripulación maldita.",
        "duracion": "143 minutos",
        "genero": "Aventura/Fantasía"
    },
    "It": {
        "proyectadaEn": "sala30",
        "descripcion": "Un grupo de niños enfrenta a una entidad aterradora que adopta la forma de un payaso.",
        "duracion": "135 minutos",
        "genero": "Terror/Suspenso"
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
            print("[3] Agregar, borrar o modificar una pelicula")
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
            print("[3] Modificar una pelicula")
            print("-------------------------------")
            
            opcion_modulo3 = input("Seleccione una opcion: ")
            if opcion_modulo3 in ["1" , "2" ,"3"]: # Sólo continua si se elije una opcion de menú válida
                if opcion_modulo3 == "1":
                    agregar_pelicula(peliculas)
                elif opcion_modulo3 == "2":
                    borrar_pelicula(peliculas)
                elif opcion_modulo3 == "3":
                    modificar_pelicula(peliculas)
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()
        
        elif opcion == "4":   # Opción 4
            mostrar_peliculas(peliculas)

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()