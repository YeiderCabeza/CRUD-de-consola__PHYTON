from Bd.conexion import ConectarBD
import funciones


def opciones():
    continuara = True
    while (continuara):
        opcionCorrecta = False
        while (not opcionCorrecta):
            print('\nAGENDA DE CONTACTOS')
            print('*' * 50)
            print('1-Crear contacto')
            print('2-Listado de contactos')
            print('3-Modificar contacto')
            print('4-Eliminar contacto')
            print('5-SALIR')
            opcion = int(input('\nseleccione una opcion: '))

            if opcion < 1 or opcion > 5:
                print('Opcion incorrecta, ingrese una opcion valida...')
            elif opcion == 5:
                continuara = False
                print("\n+++¡¡gracias por usar este programa!!+++\n")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    #  print(opcion)
    c = ConectarBD()

    if opcion == 1:
        contactos = funciones.FrmContactos()
        try:
            c.crearContactos(contactos)
        except: 
            print("Ocurrio un Error")
    elif opcion == 2:
        try:
            contactos = c.listarContactos()
            if len(contactos) > 0:
                funciones.listarConctatos(contactos)
            else:
                print("no tienes contactos")
        except: 
            print("Ocurrio un Error")
    elif opcion == 3:
        try:
            contactos = c.listarContactos()
            if len(contactos) > 0:
                contactos = funciones.FrmEditar(contactos)
                if contactos:
                    c.editar(contactos)
                else:
                    print("incorrecto no se ha encontrado el codigo a editar")
            else:
                print("no se ha encontrdo el contacto...\n")  
        except: 
            print("Ocurrio un Error")
    elif opcion == 4: 
        try:
            contactos = c.listarContactos()
            if len(contactos) > 0:
                id = funciones.FrmEliminar(contactos)
                if not (id==''):
                    c.eliminar(id)
                else:
                    print("¡¡No se ha encontrado el id!!\n")
            else:
                print("no se ha encontrdo el contacto...\n")  
        except: 
            print("Ocurrio un Error")
    else:
        print("Opcion no Valida")

opciones()
