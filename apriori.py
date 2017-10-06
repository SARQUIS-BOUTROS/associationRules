import sys
from optparse import OptionParser



# def confianzaMinima(itemFrecuente,minConf):
#     '''Falta definir'''
#
# def apGenRules(itemsFrecuentes, consecuentes, minSup,minConf,k,m):
#     hhx = consecuentes
#     reglas = [] #la idea es que tenga 2 elementos, el primero para la precondicion y el segundo para la postcondicion
#     if (k > (m+1)) and (len(consecuentes)!=0):
#         hhxx = candidateGen(hhx)
#         for h in hhxx:
#             if confianzaMinima(intemFrecuente,minConf):'''falta definir'''
#             #hacer la resta
#                 reglas[1] = #precondicion
#
# '''Falta terminar'''
# def genRules(itemsFrecunetes, minSup, minConf):
#     rule = [] # deberia tener 2 campos: 1 para el antecedente y 1 para el consecuente [1,2] -> [3,4]
#     hh1 = []
#     k=2
#     m=1
#     while (k != len(itemsFrecunetes)):
#         for items in itemsFrecunetes:
#             r = []
#             for item in items:
#                 if item == items[len(items)-1]:
#                     r[1].append(item)
#                 else:
#                     r[0].append(item)
#                 if confianzaMinima(r,minConf): # veo si la regla r que genere cumple con la confianza
#                     rule.append(r)
#                     hh1.append(r[1])
#             apGenRules(items, hh1, minSup, minConf, k, m)
#         k += 1
#         m += 1

def subsets(arr, k):
    ''''Hace todas las combinaciones de un set'''
    return chain(*[combinations(arr, k) for i, a in enumerate(arr)])

def candidateGen(setActual, k):
    #la carga ya se hizo en orden lexicografico, no hace falta ordenar aca
    ccx = [] #lista de candidatos
    ffx = setActual #set de items frecuentes
    for f1 in ffx:
        for f2 in ffx:
            agregar = False
            for item1 in f1:
                pos = f1.index(item1)
                if item1 != f2[pos]: #me fijo primero si es el ultimo elemento de la lista
                    if (pos == (len(f1)-1)):
                        agregar = True
                        break
            if agregar:
                c = f1.append(f2[pos])
                ccx.append(c.sort())
    for c in ccx:
        for subset in subsets(c, k-1):
            quitar = True
            for itemSet in ffx:
                if (subset == itemSet):
                    quitar = False
                    break
            if quitar:
                ccx.remove(c)

    return ccx

def soporteMinimo(transacciones, candidatos, minSup, k):
    itemsFrecuentes = []
    f = [k, itemsFrecuentes]
    for itemC in candidatos:
        cont = 0
        itemFrecuente = []
        for transaccion in transacciones:
            if itemC in transaccion:
                cont += 1
        if cont/len(transacciones) >= minSup:
            itemFrecuente = [itemC.sort(), cont]
            itemsFrecuentes.append(itemFrecuente)
    return f

def initPass(transacciones):
    itemSet = []
    for transaccion in transacciones:
        if transaccion not in transacciones:
            itemSet.append()
    return itemSet

def leerDocumento(archivo):
    transacciones = open(archivo, 'r') # lee el archivo
    allTransac = []
    for linea in transacciones.readlines(): # lee linea por linea el archivo
        transac = linea.split() # me transforma el string linea en una lista
        transac = map(int, transac) # mapea de letras a numeros (para string no deberia usarse)
        transac.sort() # ordena la lista
        allTransac.append(transac) # agrega a la lista de todas las transacciones
    return allTransac

def apriori (transacciones, minSup, minConf):
    cc1 = initPass(transacciones) # cc=C candidatos
    ff = soporteMinimo(transacciones, cc1, minSup, k=1) # ff=F set de items frecuentes #voy a ir acoplando las f a esta lista, haria lo mismo que el algoritmo

    k = 2
    setActual = ff
    while (len(setActual) != 0):
        ccx = candidateGen(setActual, k)
        setNuevo = soporteMinimo(transacciones, ccx, minSup, k)
        setActual = setNuevo
        ff.append(setNuevo) # agrego a la lista de todos los F
        k += 1

    for f in ff:
        print f
    # reglas = genRules(transacciones, ff, minConf)
    # return reglas

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-d', '--dataSet', dest='dataSet', help='Dataset a analizar')
    parser.add_option('-s', '--minSupport', dest='minSup', help='Minimo soporte')
    parser.add_option('-c', '--minConfidence', dest='minConf', help='Minima confianza')
    (options, args) = parser.parse_args()

    if options.dataSet is None:
        print 'No se especifico ningun dataset. Cerrando...\n'
        sys.exit('Cierre.')
    elif options.dataSet is not None:
        listaTransacciones = leerDocumento(options.dataSet)
    else:
        print 'Error de sistema.\n'
        sys.exit('Cierre.')

    reglas = apriori(listaTransacciones, options.minSup, options.minConf)
    print(listaTransacciones)
