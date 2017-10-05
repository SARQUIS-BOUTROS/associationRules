def initPass(transacciones):
    itemSet = []
    for transaccion in transacciones:
        for item in transaccion:
            if item not in itemSet:
                itemSet.append(item)
    return itemSet

def soporteMinimo(transacciones,candidatos,minSup):
    itemsFrecuentes = []
    for itemC in candidatos:
        cont = 0
        itemFrecuente = []
        for transaccion in transacciones:
            for itemT in transaccion:
                if itemC == itemT:
                    cont += 1
        if cont >= minSup:
            itemFrecuente = [itemC,cont]
            itemsFrecuentes.append(itemFrecuente)
    return itemsFrecuentes

def candidateGen(setActual):#VER SI ANDA sobre todo el ultimo for separado
    #la carga ya se hizo en orden lexicografico, no hace falta ordenar aca
    ccx = [] #lista de candidatos
    ffx = setActual #set de items frecuentes
    for f1 in ffx:
        c = f1 #lista de candidatos
        for f2 in ffx:
            set1 = f1[1].sort() # el primer elemento de los fx contienen la lista de itemsFrecuentes lo ordeno lexicograficamente por las dudas
            set2 = f2[1].sort()
            for item1 in set1:
                for item2 in set2:
                    if item1 == set1(len(set1)): #me fijo primero si es el ultimo elemento de la lista
                        if set1[len(set1)] != set2[len(set2)]: #veo si el ultimo elemento es diferente
                            c.append(set2[len(set2)])
                            ccx.append(c)
                    else:
                        if item1 != item2:
                            continue #avanza al siguiente bucle
        #hacemos la pregunta dentro del for de ffx
        for candidato in c:'''ver si no tira error aca, se esta eleminando un item donde se esta iterando por eso'''
            for item in ffx:
                if candidato not in item[1]:#el primer element de ffx seria el nombre del item el segundo es la cantidad de beces que aparece
                    ccx.remove(c)
    return ccx


def apriori (transacciones):
    cc1 = initPass(transacciones) # cc=C candidatos
    ff = soporteMinimo(cc1) # ff=F set de items frecuentes #voy a ir acoplando las f a esta lista, haria lo mismo que el algoritmo

    #k = 2 #no lo uso
    setActual = ffx
    while (len(setActual) != 0):
        ccx = candidateGen(setActual)
        '''falta las preguntas esas'''
        setNuevo = soporteMinimo(ccx)
        setActual = setNuevo
        #k += 1
        ff.append(setNuevo)#agrego a la lista de todos los F
    return ff

##GenerarReglas

def confianzaMinima(itemFrecuente,minConf):
    '''Falta definir'''

def apGenRules(itemsFrecuentes, consecuentes, minSup,minConf,k,m):
    hhx = consecuentes
    reglas = [] #la idea es que tenga 2 elementos, el primero para la precondicion y el segundo para la postcondicion
    if (k > (m+1)) and (len(consecuentes)!=0):
        hhxx = candidateGen(hhx)
        for h in hhxx:
            if confianzaMinima(intemFrecuente,minConf):'''falta definir'''
            #hacer la resta
                reglas[1] = #precondicion
'''Falta terminar'''
def genRules(itemsFrecunetes, minSup, minConf):
    rule = []#deberia tener 2 campos: 1 para el antecedente y 1 para el consecuente [1,2] -> [3,4]
    hh1 = []
    k=2
    m=1
    while (k!=len(itemsFrecunetes)):
        for items in itemsFrecunetes:
            r = []
            for item in items:
                if item == items(len(items)):
                    r[2].append(item)
                else:
                    r[1].append(item)
                if confianzaMinima(r,minConf):#veo si la regla r que genere cumple con la confianza
                    rule.append(r)
                    hh1.append(r[2])
            apGenRules(items,hh1,minSup,minConf,k,m)
        k += 1
        m += 1
