from itertools import chain,combinations
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))


def transicion(estado,sigma):
    global delta
    print(estado,sigma)
    estado_siguiente = delta[(estado,sigma)]
    print("transicion(",estado,",",sigma,")->",estado_siguiente)
    return estado_siguiente


Q = ['q0','q1','q2','q3','q4']
s = 'q0'
F = ['q1']
sprima = (s,)
sigma = ['a','b']

DELTA =  { ('q0','a'):['q0','q3'],
           ('q0','b'):['q0','q1'],
           ('q1','b'):['q2'],
           ('q2','a'):['q2'],
           ('q2','b'):['q2'],
           ('q3','a'):['q4'],
           ('q4','a'):['q4'],
           ('q4','b'):['q4']}

Qprima = list(powerset(Q))

Fprima = []

for q in Qprima:
    for x in q:
        if x in F:
            Fprima.append(q)
print Fprima
delta = {}

for qprima in Qprima:
    for s in sigma:
        #print(qprima,s)
        P = [] ; #print("Detectando los estados p a donde se puede llegar con",s,"desde",qprima)
        for q in qprima:
            if(q,s) in DELTA.keys():
                #print("DELTA[(",q,",",s,")]",DELTA[(q,s)])
                for p in DELTA[(q,s)]:
                    if not (p in P): P.append(p)
        #print("P=",P)
        if len(P)>0: P.sort()
        delta[(qprima,s)] = tuple(P)
        print("delta(",qprima,",",s,")=",delta[(qprima,s)])


ejemplos = ["a","b","aaa","baaa","aaaaaaba","abbb"]


for w in ejemplos:
    estado = sprima
    for c in w:
        estado = transicion(estado,c)
    if estado in Fprima:
        print("{} si esta en el lenguaje".format(w))
    else:
        print("{} No esta en el lenguaje".format(w))
