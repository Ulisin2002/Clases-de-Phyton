def salir():
    print("Gracias por usar nuestro programa")
def registrar_trabajador():
    
    nombre=input("Ingrese el nombre del trabajador : ")
    for trabajador in trabajadores:
        if trabajador[0] == nombre:
            print("Este trabajador ya está registrado.")
            return None
    if len(nombre)<=3:
        print("Debe ingresar un nombre con mas de 3 caracteres")
    else:
        print("Ingrese su cargo : ")
        print("1) Programador")
        print("2. CEO")
        print("3. Analista ")
        opcioncargo=int(input(""))
        if opcioncargo==1:
            print("Ha elegido Programador")
            cargo="Programador"
        elif opcioncargo==2:
            print("Ha elegido CEO")
            cargo="CEO"
        elif opcioncargo==3:
            print("Ha elegido Analista")
            cargo="Analista"
        else:
            print("Opcion no valida")
            return None    
        try:
            sueldoBruto=int(input("Ingrese el sueldo bruto : "))
        except ValueError:
            print("Debe ingresar valor numerico")
        else:
            #calculo descuentos:
            descuentoSalud= sueldoBruto*0.07
            descuentoAFP=sueldoBruto*0.12
            #calculo sueldo liquido
            sueldoLiquido=sueldoBruto-descuentoSalud-descuentoAFP
            trabajador= nombre,cargo,sueldoBruto,descuentoSalud, descuentoAFP, sueldoLiquido
            trabajadores.append(trabajador)
            print("Volviendo al menu...")
            print("-------------------------")
            return trabajador
    
def mostrar_trabajadores():
    
    if len(trabajadores)==0:
        print("Primero debe registrar un trabajador")
    else:
        print("Estos son todos los trabajadores registrados")
        print("--------------------------------------------")
        for trabajador in trabajadores:
            print("--------------------------------")
            print("Nombre:", trabajador[0])
            print("Cargo:", trabajador[1])
            print("Sueldo bruto", trabajador[2])
            print("Descuento salus", trabajador[3])
            print("Descuento AFP", trabajador[4])
            print("Sueldo liquido:", trabajador[5])
            print("--------------------------------")
def imprimir_planilla_de_sueldos():
    
    print("1. Imprimir planilla de todos los trabajadores")
    print("2. Imprimir la plantilla de un trabajador")
    print("3. Imprimir plantilla de sueldos por cargos")
    opcion=input("")
    
    if opcion == '1':
        if len(trabajadores) == 0:
            print("No hay trabajadores registrados")
        else:
            print("Imprimiendo planilla de sueldos de todos los trabajadores...")
            with open('planilla_sueldos.txt', 'w') as archivo:
                archivo.write("Planilla de sueldos de todos los trabajadores:\n")
                for trabajador in trabajadores:
                    archivo.write(f"Nombre: {trabajador[0]}\n")
                    archivo.write(f"Cargo: {trabajador[1]}\n")
                    archivo.write(f"Sueldo bruto: {trabajador[2]}\n")
                    archivo.write(f"Descuento salud: {trabajador[3]}\n")
                    archivo.write(f"Descuento AFP: {trabajador[4]}\n")
                    archivo.write(f"Sueldo líquido: {trabajador[5]}\n")
                    archivo.write("--------------------------------\n")
            print("Planilla de sueldos de todos los trabajadores guardada en 'planilla_sueldos.txt'")
    if opcion=="2":
        nombre_verificacion = input("Ingrese el nombre del trabajador que desea ver su planilla: ")
        for trabajador in trabajadores:
            if trabajador[0] == nombre_verificacion:
                with open('planilla_sueldos.txt', 'w') as archivo:
                    archivo.write(f"Nombre: {trabajador[0]}\n")
                    archivo.write(f"Cargo: {trabajador[1]}\n")
                    archivo.write(f"Sueldo bruto: {trabajador[2]}\n")
                    archivo.write(f"Descuento salud: {trabajador[3]}\n")
                    archivo.write(f"Descuento AFP: {trabajador[4]}\n")
                    archivo.write(f"Sueldo líquido: {trabajador[5]}\n")
                    print("Planilla de sueldos del trabajador guardada en 'planilla_sueldos.txt'")
                break
        else:
            print("Nombre no encontrado")
    if opcion=="3":
        print("Seleccione el cargo:")
        print("1) Programador")
        print("2) CEO")
        print("3) Analista")
        seleccionarcargo = int(input("Ingrese el número correspondiente al cargo: "))
        # Verificar si hay trabajadores registrados bajo el cargo seleccionado
        hay_trabajadores = False
        for trabajador in trabajadores:
            if seleccionarcargo == 1 and trabajador[1] == "Programador":
                hay_trabajadores = True
                break
            elif seleccionarcargo == 2 and trabajador[1] == "CEO":
                hay_trabajadores = True
                break
            elif seleccionarcargo == 3 and trabajador[1] == "Analista":
                hay_trabajadores = True
                break
        
        if not hay_trabajadores:
            print("No hay trabajadores registrados bajo ese cargo")
            return None
        
        if seleccionarcargo == 1:
            print("Imprimiendo planilla de sueldos para Programadores...")
            with open('planilla_programadores.txt', 'w') as archivo:
                archivo.write("Planilla de sueldos de Programadores:\n")
                for trabajador in trabajadores:
                    if trabajador[1] == "Programador":
                        archivo.write(f"Nombre: {trabajador[0]}\n")
                        archivo.write(f"Cargo: {trabajador[1]}\n")
                        archivo.write(f"Sueldo bruto: {trabajador[2]}\n")
                        archivo.write(f"Descuento salud: {trabajador[3]}\n")
                        archivo.write(f"Descuento AFP: {trabajador[4]}\n")
                        archivo.write(f"Sueldo líquido: {trabajador[5]}\n")
                        archivo.write("--------------------------------\n")
            print("Planilla de sueldos de Programadores guardada en 'planilla_programadores.txt'")
        
        elif seleccionarcargo == 2:
            print("Imprimiendo planilla de sueldos para CEO...")
            with open('planilla_ceo.txt', 'w') as archivo:
                archivo.write("Planilla de sueldos de CEO:\n")
                for trabajador in trabajadores:
                    if trabajador[1] == "CEO":
                        archivo.write(f"Nombre: {trabajador[0]}\n")
                        archivo.write(f"Cargo: {trabajador[1]}\n")
                        archivo.write(f"Sueldo bruto: {trabajador[2]}\n")
                        archivo.write(f"Descuento salud: {trabajador[3]}\n")
                        archivo.write(f"Descuento AFP: {trabajador[4]}\n")
                        archivo.write(f"Sueldo líquido: {trabajador[5]}\n")
                        archivo.write("--------------------------------\n")
            print("Planilla de sueldos de CEO guardada en 'planilla_ceo.txt'")
        
        elif seleccionarcargo == 3:
            print("Imprimiendo planilla de sueldos para Analistas...")
            with open('planilla_analistas.txt', 'w') as archivo:
                archivo.write("Planilla de sueldos de Analistas:\n")
                for trabajador in trabajadores:
                    if trabajador[1] == "Analista":
                        archivo.write(f"Nombre: {trabajador[0]}\n")
                        archivo.write(f"Cargo: {trabajador[1]}\n")
                        archivo.write(f"Sueldo bruto: {trabajador[2]}\n")
                        archivo.write(f"Descuento salud: {trabajador[3]}\n")
                        archivo.write(f"Descuento AFP: {trabajador[4]}\n")
                        archivo.write(f"Sueldo líquido: {trabajador[5]}\n")
                        archivo.write("--------------------------------\n")
            print("Planilla de sueldos de Analistas guardada en 'planilla_analistas.txt'")
        else:
            print("Opción no válida")
        

opcionprincipal=5
trabajadores=[]
while opcionprincipal!=4: 
    
    print("1. Registrar trabajador")
    print("2. Mostrar trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del programa")
    opcionprincipal=int(input("Ingrese su opcion : "))
    
    match opcionprincipal:
        case 1:
            registrar_trabajador()
            
        case 2:
            mostrar_trabajadores()
            
        case 3:
            imprimir_planilla_de_sueldos()
            
        case 4:
            salir()
            break
         