# CASO 4
# Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones.

# Añadir contacto
# Lista de contactos
# Buscar contacto
# Editar contacto
# Cerrar agenda
import os
import time


if os.name == "posix":
    var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"

class contacto():
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email     
    
    def __str__(self):
        return f'\n nombre: {self.nombre}\n telefono: {self.telefono} \n email: {self.email}'



class lista_contacto():
    def __init__(self):
        self.lista_de_contacto = []

    def agregar_contacto(self, contact):
        self.lista_de_contacto.append(contact)

    def __str__(self):              
        self.contactos_str = 'Esta es la lista de sus contactos: \n'
        indice = 0
        for cont in self.lista_de_contacto:
            indice +=1
            self.contactos_str += f'\n{indice}:\n {cont}\n'

        return f'{self.contactos_str}'

    def buscar_conctacto(self, dato):
        contactos_coincidentes = ''        
        
        for contacto in self.lista_de_contacto:            
            if dato in [contacto.nombre, contacto.telefono, contacto.email]:
                contactos_coincidentes += f"{contacto} \n"
        if contactos_coincidentes == '':
            return 'usuario inexistente'               
        else: return f'Los siguientes usuario coinciden con su busqueda \n {contactos_coincidentes}'

    def editar_conctacto(self, contacto_buscado, dato_a_editar, nuevo_dato):        
        self.dato_a_editar = dato_a_editar
        self.nuevo_dato = nuevo_dato
        self.contacto_buscado = contacto_buscado
        
        for contacto in self.lista_de_contacto:
            if self.contacto_buscado in [contacto.nombre, contacto.telefono, contacto.email]:
                print(f'{contacto}\n')
                opcion = input('quirere modificar este usuario? si o no: ')
                while not opcion in ['si', 'no']:
                    opcion = input('quirere modificar este usuario? si o no: ').lower()
                if opcion == 'si':
                    if self.dato_a_editar == '1':
                        print(f'\ncambiaste el nombre de contacto: {contacto.nombre} por ', end='')
                        contacto.nombre = self.nuevo_dato
                        print(contacto.nombre)
                    elif self.dato_a_editar == '2':
                        print(f'\ncambiaste el numero de telefono de contacto: {contacto.telefono} por ', end='')
                        contacto.telefono = self.nuevo_dato
                        print(contacto.telefono)
                    elif self.dato_a_editar == '3':
                        print(f'\ncambiaste el mail de contacto: {contacto.telefono} por ', end='')
                        contacto.email = self.nuevo_dato
                        print(contacto.email)
                    return print(f'{contacto} \n')
                    


                    
        
                

def pociones_posibles(cadena):
    while not cadena in ['1', '2', '3']:
        print('Ingrese una de las opciones (1, 2, 3)')
        cadena = input('')
    return cadena



listaContacto = lista_contacto()    

while True:
    
    opcion = input('MENU OPCIONES: \n\t1. Añadir contacto \n\t2. Lista de contactos \n\t3. Buscar contacto \n\t4. Editar contacto \n\t5. Cerrar agenda\n ')

    if opcion in ['1', '2', '3', '4', '5']:
        if opcion == '1':
            nombre, telefono, email = input('nombre: '), input('telefono: '), input('email: ')
            contact = contacto(nombre, telefono, email)
            listaContacto.agregar_contacto(contact)
            
        elif opcion == '2':
            print(listaContacto)
            time.sleep(3)

        elif opcion == '3':
            buscado = input('Ingrese nombre, telefono o email: ')
            print(listaContacto.buscar_conctacto(buscado))
            
            
        elif opcion == '4':
            usuario_a_editar = input('ingrese usuario a modificar (nombre, telefono o mail): ')
            
            print(listaContacto.buscar_conctacto(usuario_a_editar))

            if not listaContacto.buscar_conctacto(usuario_a_editar) == 'usuario inexistente':

                dato_a_editar = pociones_posibles(input('Que dato quiere modificar: 1: nombre, 2: telefono, 3: email: '))

                nuevo_valor = input('\ningrese nuevo dato: ')

                listaContacto.editar_conctacto(usuario_a_editar, dato_a_editar, nuevo_valor)
                time.sleep(3)

                
                
            else: print('Vuelva a intentar')
               

          
        
        else:
            print('\nMuchas gracias vuelva pronto')
            break
           


    else: print('\nOPCION INCORRECTA. Vuelva intentarlo. ')   

    time.sleep(2)
    os.system(var)

time.sleep(2)
os.system(var)
