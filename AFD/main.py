
sigma  = ['a','b'] #alfabeto
Q = ['q0','q1'] #Conjunto de estados
s = 'q0' #Estado inicial
F = ['q1'] #Estado final


delta = { ('q0','a'):'q0',
          ('q0','b'):'q1',
          ('q1','a'):'q0',
          ('q1','b'):'q1' }


ejemplos = ['abab','bb','bababb','bbbbbb','abaaa','abbb','bbbb']

def cambio_estado(q,s):
    global delta
    return delta[(q,s)]


for w in ejemplos:
    estado = s
    for c in w:
        estado = cambio_estado(estado,c)
    if estado in F:
        print("{} si esta en el lenguaje".format(w))
    else:
        print("{} No esta en el lenguaje".format(w))
