import os
import modulos.notas as n


def Principal()->int:
    titulo='''
        ++++++++++++++++++++++++++++++
        +     Estudiantes Campus     +
        ++++++++++++++++++++++++++++++
    '''

    os.system('cls')

    opciones=['1.Agregar estudiante\n2.Agregar nota\n3.Borrar estudiante\n4.Reportes\n5.Salir\n']
    print(titulo)
    for i in opciones:
        print(i)
    op=int(input('Elige una opcion: ')) 

    return op



def opcion2(soruce:dict):
    titulo='''
        +++++++++++++++++++++++++++++++++++
        +         Agregar notas           +
        +++++++++++++++++++++++++++++++++++
    '''
    
   
    
    validar1=True
    while validar1:
       
        os.system('cls')
        print(titulo)
        print('Que tipo de nota desea agregar')
        print('1.Agregar nota de Parcial\n2.Agregar Nota de quices\n3.Agregar nota de trabajos\n4.salir\n')

        op= int(input('Elige una opcion: '))
        if op==1:
            n.notaParcial(soruce)
        elif op==2:
            n.notaQuizz(soruce)
        elif op==3:
            n.notaTrabajo(soruce)
            
        elif op==4:
            n.notaFinal(soruce)
            validar1=False
        else:
            print('ingresa un valor valido')


def mostrarInformacion(source:dict):
    titulo='''
            ++++++++++++++++++++++++++++++
            +   Informacion estudiantes  +
            ++++++++++++++++++++++++++++++
        '''

    os.system('cls')
    print(titulo)
    op=str(input('Ingrese el nombre del estudiante: ')).capitalize()

    for key,value in source.items():
        if op in value['nombre']:
            print('Nombre :',value['nombre'])
            print('Edad',value['edad'])
            print('Notas:',value['notas'])
            print('Nota Final:',value['notaFinal'])
