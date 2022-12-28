#Importa pandas
import pandas as pd

#Leer los datos de los clientes desde el CSV
df = pd.read_csv('./datos_clientes.csv')
print(df.head())
#Diccionario vacio donde se va a almacenar los atributos de los clientes
clientes = {}

#Funcion para agregar clientes (1)
def agregar_cliente():
    global clientes

    try:
        dni = int(input('Ingrese un DNI: '))
        nombre = input('Ingrese un nombre y apellido: ')
        direccion = input('Ingrese una dirección: ')
        telefono = int(input('Ingrese un número de teléfono: '))
        mail = input('Ingrese un correo electrónico: ')
        preferente = input('¿El cliente es preferente? Ingrese S/N: ')

        clien = {
            'nombre':nombre,
            'dni':dni,
            'direccion':direccion,
            'telefono':telefono,
            'mail':mail,
            'preferente':preferente=='S'
        }
        
    except ValueError:
        print('****** INGRESE UN VALOR VÁLIDO ******')
    else:
        clientes[dni] = clien

        df = pd.read_csv('./datos_clientes.csv')

        # Insertar nueva fila al archivo CSV
        df.loc[len(df.index)] = [dni, nombre, direccion, telefono, mail, preferente]
        
        # Guardar cambios en el CSV original
        df.to_csv('./datos_clientes.csv', index=False)
        
        
        return print('****** CLIENTE AGREGADO CON ÉXITO ******')


#Funcion para eliminar un cliente usando su dni (2)
def borrar_cliente():
    try:
        cliente_dni = int(input("Ingrese el DNI del cliente a eliminar: "))
        if cliente_dni in clientes:

            #Borrar fila en el archivo CSV
            df.drop(df.index[(df["dni"] == Dni)], axis=0, inplace=True)

            # Report_Card.drop(Report_Card.index[(Report_Card["Lectures"] == "German")],axis=0,inplace=True)

            #Guardar cambios en el CSV original
            df.to_csv('./datos_clientes.csv')

            print('*****************************************')
            print('****** CLIENTE ELIMINADO CON ÉXITO ******')
            print('*****************************************')
        else:
            print('**************************************************')
            print('*** NO EXISTE CLIENTE CON EL DNI: ', cliente_dni,' *****')
            print('**************************************************')
    except ValueError:
        print("****** POR FAVOR INGRESE UN DNI VÁLIDO ****** \n")


#Funcion para mostrar datos de todos los clientes (3)
def mostrar_datos_cliente():
    
    try:
        dni_cliente = int(input('Ingrese el DNI del cliente: '))
        for key, value in clientes.items():
            if dni_cliente in clientes:
                print("DNI: ", value['dni'], "Nombre: ", value['nombre'])
                
            else:
                print('**************************************************')
                print('****** NO EXISTE CLIENTE O DNI INCORRECTO ******')
                print('**************************************************')

    except ValueError:
        print("****** POR FAVOR INGRESE UN DNI VÁLIDO ****** \n")

#Funcion para listar a todos los clientes (4)
def listar_clientes():

    try:
        for cliente in clientes:
            if cliente in clientes:
                print('****** LISTA DE CLIENTES ******')
                print('*******************************')
                for key, value in clientes.items():
                    print(df)
                    print("DNI: ", value['dni'], "Nombre: ", value['nombre'])
                    break
                else:
                    print('****** NO EXISTEN CLIENTES ******')
                    print('*********************************')
    finally:
        print("****** Para agregar un nuevo cliente ingrese opcion (1) ****** \n")

#Funcion para ver los clientes preferentes (5)
def listar_clientes_pref():

    try:
        for key,value in clientes.items():
            if value['preferente'] == True:
                print('****** LISTA DE CLIENTES PREFERENTES ******')
                print('*******************************************')
                print("DNI: ", value['dni'], "Nombre: ", value['nombre'])
                break
            else:
                print('*****************************************')
                print('****** NO HAY CLIENTES PREFERENTES ******')
                print('*****************************************')
    finally:
        print("****** Para agregar un cliente ingrese opcion (1) ****** \n")



#MENU DE OPCIONES
while True:
        print("******* MENÚ *******\n"
            "1. Añadir cliente: \n"
            "2. Eliminar cliente: \n"
            "3. Mostrar datos de un cliente: \n"
            "4. Listar todos los clientes con nombre y DNI: \n"
            "5. Listar clientes preferentes con nombre y DNI: \n"
            "6. Salir.\n")

        opcion = int(input('Selecciona una opcion: '))

        if opcion==1:
            agregar_cliente()
        elif opcion==2:
            borrar_cliente()
        elif opcion==3:
            mostrar_datos_cliente()
        elif opcion==4:
            listar_clientes()
        elif opcion==5:
            listar_clientes_pref()
        elif opcion==6:
            exit(0)
        else:
            print('****** OPCIÓN INVÁLIDA ****** \n')