opcion=0
import random
numeroazar=random.randint(1,3)

generos=["comic", "novela","manga","ciencia","humor"]
def crear_libro():
    titulo = input("Ingrese el nombre del producto: ")
    print("Eliga el genero: ")
    print("1. Comic")
    print("2. Novela")
    print("3. Manga")
    print("4. Ciencia")
    print("5. Humor")
    try:
        genero=int(input(""))
    except ValueError:
        print("Ingrese numeros.")
    else:
        if genero==1:
            genero="Comic"
        elif genero==2:
            genero="Novela"
        elif genero==3:
            genero="Manga"
        elif genero==4:
            genero="Ciencia"
        elif genero==5:
            genero="Humor"
        else:
            print("Opcion no valida")
            return None
    while True:
        try:
            precio = int(input("Ingrese el precio del libro: "))
            stock = int(input("Ingrese el stock del libro: "))
        except ValueError:
            print("El precio y el stock deben ser números enteros.")
        else:
            if precio == 0 or stock == 0:
                print("El precio y el stock deben ser mayores o iguales a cero.")
            else:
                libro = [titulo, genero, precio,stock]
                precio_total=libro[2]*libro[3]
                print("El precio sera de: " , precio_total)
                libro = [titulo, genero, precio,stock, precio_total]
                return libro

libros = []

def registrar_producto(libro):
    print(libro)
    for L_guardado in libros:
        if L_guardado[0] == libro[0]:
            L_guardado[0] = L_guardado[0]
            L_guardado[1] = libro[1]
            L_guardado[2] = L_guardado[2]=libro[2]
            L_guardado[3] = L_guardado[3]+libro[3]
            L_guardado[4] = L_guardado[4]+libro[4]
            return producto
    libros.append(libro)

def lista_de_productos():
    for li in libros:
        print(f"Nombre: {li[0]}, Genero: {li[1]}, Precio: {li[2]},Stock {li[3]},Precio total : {li[4]}")


def imprimir_pedidos():
    if not libros:
        print("Primero debe pedir libros")
    else: 
        with open('lista_de_libros', 'w') as archivo:
            archivo.write("Lista de los libros pedidos:\n")
            for libro in libros:
                    archivo.write(f"Titulo: {libro[0]}\n")
                    archivo.write(f"Genero: {libro[1]}\n")
                    archivo.write(f"Precio: {libro[2]}\n")
                    archivo.write(f"Stock: {libro[3]}\n")
                    archivo.write(f"Precio total: {libro[4]}\n")
                    archivo.write("--------------------------------\n")
            print("Lista de todos los libros guardada en 'lista_de_libros.txt'")
def salir():
    print("Gracias por usar nuestro programa UwU")
    
while opcion!=5:
    print("LLegaron estos lotes de libros: ", numeroazar)
    print("1. Crear libro")
    print("2. Registrar libro")
    print("3. Lista de los libros")
    print("4. Generar archivo")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            producto = crear_libro()
        case 2:
            registrar_producto(producto)
        case 3:
            lista_de_productos()
        case 4:
            imprimir_pedidos() 
        case 5:
           salir()
