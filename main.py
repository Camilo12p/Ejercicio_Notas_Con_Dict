import modulos.menu as m
import modulos.estudiante as e
import os

validar=True
campus={}


while validar:
    try:
        op= m.Principal()
       
        if op==1:
            e.agregarestudiante(campus)
            print(campus)
            os.system('pause')  
        elif op==2:
            m.opcion2(campus)
            print(campus)
            os.system('pause')
            pass
        elif op==3:
            e.eliminarestudiante(campus)  
            print(campus)          
            os.system('pause')
            pass
        elif op==4:
            m.mostrarInformacion(campus)
            os.system('pause')

        elif op==5: 
            validar=False
            os.system('pause')
        else:
            print('ingresa un valor valido')
            os.system('pause')
    except ValueError:
        print('ingresa un valor valido')
        os.system('pause')
