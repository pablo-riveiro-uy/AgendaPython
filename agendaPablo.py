agenda = [
    {
        'nombre': 'Pablo',
        'telefono': '094539027',
        'direccion': 'Agustin Muñoz 4777'
    },
    {
        'nombre': 'Luciana',
        'telefono': '099739025',
        'direccion': 'Santiago Danuzio 2660'
    },
]


def getPersona(buscado):
    encontro = False
    if buscado == None:
        buscado = input("Buscar a ?: ")
        print('*****')
    for i in agenda:
        if i['nombre'] == buscado:
            print(i['nombre'])
            print(i['telefono'])
            print(i['direccion'])
            encontro = True
    if encontro != True:
        print(buscado+" No está en la lista")


def borrar():
    aBorrar = input("Buscar a ?: ")
    getPersona(aBorrar)
    respuesta = input("borrar ? s/n ")
    if respuesta == 's':
        for i in range(0, len(agenda)-1):
            if agenda[i]['nombre'] == aBorrar:
                del agenda[i]
                print("contacto borrado \n")
    else:
        print("No se borró ningún contacto \n")
    menu()


def menu():

    print('\n AGENDA')
    print('-----')
    print('1 Buscar Contacto, 2 Agregar contacto, 3 Borrar Contacto, 4 Mostrar lista completa')
    print("\n")
    respuesta = input("OPCION ?")
    if respuesta == '1':
        getPersona(None)
        menu()
    elif respuesta == '2':
        agregar()
    elif respuesta == '3':
        borrar()
    elif respuesta == '4':
        mostrarTodo()
    else:
        print("no es una opcion \n")
        menu()


def mostrarTodo():
    for i in agenda:
        print("Nombre: " + i['nombre'])
        print("Telefono: " + i['telefono'])
        print("Direccion: " + i['direccion'])
        print("---------------")
    menu()


def agregar():
    nuevoUsuario = {
        'nombre': "Nombre",
        'telefono': 000000,
        'direccion': 'Direccion'
    }
    nuevoUsuario['nombre'] = input("Nombre: ")
    nuevoUsuario['telefono'] = input("Tel: ")
    nuevoUsuario['direccion'] = input("Direccion: ")
    agenda.append(nuevoUsuario)
    print("CONTACTO AGREGADO \n")
    menu()


menu()