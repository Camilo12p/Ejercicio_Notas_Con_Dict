
def agregarestudiante(source:dict):
   
    nombre=input('ingrese el nombre del estudiante: ').capitalize()
    edad=int(input('ingrese la edad: '))
    estudiante={
        'nombre':nombre,
        'edad':edad,
        'notas':{
            'quices':{},
            'parciales':{},
            'trabajos':{}
        
        },
        'notaFinal':0
       
     }
    source.update({len(source)+1:estudiante})

    op=bool(input("Desea añadir otro estudiante:\nPresiona S para si\nPresiona ENTER para no\n"))
    if(op==True):
        agregarestudiante(source)


def eliminarestudiante(soruce:dict):
    nombre=input('Ingrese el nombre del estudiante a eliminar: ').capitalize()
    for key, value in soruce.items():
        if nombre in value['nombre']:
            soruce.pop(key)
            break
