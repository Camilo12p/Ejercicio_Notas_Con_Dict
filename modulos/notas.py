def notaParcial(source:dict):
    estudiante=str(input('Nombre del estudiante a agregar notas: ')).capitalize()
    nota= float(input('Nota del Parcial: '))
    
    for key,value in source.items():
        if estudiante in value['nombre']:
            value['notas']['parciales'].update({len(value['notas']['parciales'])+1:nota})


def notaQuizz(source:dict):
    estudiante=str(input('Nombre del estudiante a agregar notas: ')).capitalize()
    nota= float(input('Nota del Quizz: '))
    
    for key,value in source.items():
        if estudiante in value['nombre']:
            value['notas']['quices'].update({len(value['notas']['quices'])+1:nota})

def notaTrabajo(source:dict):
    estudiante=str(input('Nombre del estudiante a agregar notas: ')).capitalize()
    nota= float(input('Nota del Trabajo: '))
    
    for key,value in source.items():
        if estudiante in value['nombre']:
            value['notas']['trabajos'].update({len(value['notas']['trabajos'])+1:nota})


def notaFinal(source:dict):
    totalQuiz=0
    sumaQuiz=0
    sumaTrabajos=0
    sumaParciales=0
    totalTrabajos=0
    totalParcial=0
    for key,value in source.items():
        
        sumaQuiz=0
        for idx in range(len(value['notas']['quices'])):
            sumaQuiz+=value['notas']['quices'][idx+1]
            
        totalQuiz=sumaQuiz/len(value['notas']['quices'])
           

   
        idx=1
        sumaTrabajos=0
        for idx in range(len(value['notas']['trabajos'])):
            sumaTrabajos+=value['notas']['trabajos'][idx+1]
            idx+=1
        totalTrabajos=sumaTrabajos/len(value['notas']['trabajos'])
            
    
        idx=1
        sumaParciales=0
        for idx in range(len(value['notas']['parciales'])):
            sumaParciales+=value['notas']['parciales'][idx+1]
            idx+=1
        totalParcial=sumaParciales/len(value['notas']['parciales'])

        value['notaFinal']=(totalParcial)*0.7 + (totalQuiz)*0.2 + (totalTrabajos)*0.1    



    