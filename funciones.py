def listarConctatos(contactos):
    print("\ncontactos: \n")
    print('*' * 50)
    contador = 1
    for con in contactos:
        datos = "{0}. id: {1} | Nombres: {2} | Apellidos: {3} | Telefono:({4}) | gmail: {5}"
        print(datos.format(contador, con[0], con[1], con[2], con[3], con[4]))
        contador = contador + 1
    print(" ")


def FrmContactos():
    valtel = False
    nombres = input("\nNombres : ")
    apellidos = input("Apellidos: ")
    while (not valtel):
        telefono = input("Telefono: ")
        if telefono.isnumeric():
            if (int(telefono) > 0):
                valtel = True
                telefono = int(telefono)
            else:
                print("incorrecto: debe ser un numero mayor a ceo")
        else:
            print("incorrecto, debe ser un numero")

    correo = input("Correo: ")
    print(" ")

    contactos = (nombres, apellidos, telefono, correo)
    return contactos


def FrmEliminar(contactos):
    listarConctatos(contactos)
    exiteid = False
    id = int(input("ingrese el id del conctato que desee eliminar: "))
    print(" ")
    for con in contactos:
        if con[0] == id:
            exiteid = True
            break

    if not exiteid:
        id = ""

    return id


def FrmEditar(contactos):
    listarConctatos(contactos)
    exiteid = False
    id = int(input("ingrese el id del conctato que desee editar: "))
    print(" ")
    for con in contactos:
        if con[0] == id:
            exiteid = True
            break

    if exiteid:
        valtel = False
        nombres = input("\nNombres : ")
        apellidos = input("Apellidos: ")
        while (not valtel):
            telefono = input("Telefono: ")
            if telefono.isnumeric():
                if (int(telefono) > 0):
                    valtel = True
                    telefono = int(telefono)
                else:
                    print("incorrecto: debe ser un numero mayor a ceo")
            else:
                print("incorrecto, debe ser un numero")

        correo = input("Correo: ")
        print(" ")

        contactos = (id, nombres, apellidos, telefono, correo)
    else:
        contactos = None

    return contactos

