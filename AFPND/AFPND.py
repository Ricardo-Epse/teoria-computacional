def saca_mete(c,pila):
    if c is 'e':
        pila.pop()
    elif c is 'Z':
        print"no hago nada"
    else:
        pila.append(c)
    
    
        
def transicion(estado , sigma , gamma):
    global delta ,Sigma, Gamma ,pila
    estado_sig = list(delta[(estado,sigma,gamma)])
    print estado_sig
    saca_mete(estado_sig[1],pila)
    print(pila)
    return estado_sig[0]


pila = ['Z']
Q =  ['q0','q1']
s = 'q0'
Sigma = ['a','b','w']
Gamma = ['A','Z']
F = ['q2']

delta  = {
            ('q0','w','Z'):('q1','Z'),
            ('q0','a','Z'):('q0','A'),
            ('q0','a','A'):('q0','A'),
            ('q0','w','A'):('q1','Z'),
            ('q1','b','A'):('q1','e'),
            ('q1','','Z'):('q2','Z'),
            
          
            }


ejemplos = ["aawbb","w",'awbb','bwa']


for w in ejemplos:
    estado = s
    try:
        for c in w:
            estado = transicion(estado,c,pila[-1])
        estado = transicion(estado,'',pila[-1])
        if estado in F:
            print("La cadena {} es valida").format(w)
        else:
            print("La cadena {} no valida").format(w)
    except:
        print("Error")






    

