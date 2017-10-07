def confianzaMinima(transacciones, f, reglaCandidata, minConf):
    #faux.append(reglaCandidata[1])
    #faux.extend(reglaCandidata[2])#uno las dos partes asi me genera una sola lista con todos los elementos, itemsf es una lista de dos elementos, el antecedente y el consecuente
    antecedente = reglaCandidata[1]
    fcont = 0 #contador f
    antcont = 0 #contador antecedente de itemsf o sea itemsf[1]
    for transaccion in transacciones:
        cont = 0 #renuevo por cada transaccion
        for item in f:
            if item in transaccion:
                cont += 1 #voy sumando la cantidad de veces que coinciden los elementos en la transaccion individual
            if cont == len(f): #si coinciden todos le sumo 1 ya que esos elementos aparecen en la transaccion
                fcont += 1
            if (item in antecedente) and (item in transaccion): #quiere decir que el item de f tambien es un antecedente
                antcont += 1
    if antcont != 0:#quitar despues
        confianza = fcont/antcont
        if confianza >= minConf:
            return True
        return False
    else: return False

def genRules (transacciones, itemsFrecuentes, minSup, minConf):
    reglas = []
    for f in itemsFrecuentes:
        if len(f[0]) >= 2:
            aux = f[0]
            for item in f[0]:
                antecedentes = []
                consecuente = [item]
                i = 0
                while i != len(f[0]):
                    if aux[i] != item:
                        antecedentes.append(aux[i])
                    i += 1
                regla = [antecedentes,consecuente]
                print(regla)



'''#la idea del codigo anterior es [1,2,3] toma primero el 1 lo agrega como consecuente y lo que queda de la lista es precedente, asi va haciendo en el bucle
    reglas = []
    hh1 = []
    for f in itemsFrecuentes:
        itemSet = f[0]
        k = len(f[0])
        if k >= 2:
            aux = itemSet#tiene todos los elementos
            regla = []
            for item in itemSet:
                aux.remove(item)
                antecedentes = aux
                consecuente = [item]
                regla.append(antecedentes)
                regla.append(consecuente)
                #antecedentes y un consecuente, aux ya es una lista
                #if (confianzaMinima(transacciones, f, aux2, minConf)):

                reglas.append(regla)
                #    hh1.append(item)

        #reglas.extend(apGenRules(f, hh1, k, m = 1)) #concateno la lista de un elemento con la de mas de un elemento
    return reglas
'''
'''
    def apGenRules(f, hh, k, m):
        if (k > (m + 1)) and (len(hh) != 0):
            hhx = candidateGen(hh)
            cantAntecedentes = 1 #cantidad de antecedentes
            for h in hhx:
                regla = []
                aux = h
                aux2 = []
                aux3 = aux
                aux4 = []
                cont = 0
                cont2 = 0 #por si termina la lista tiene que volver atras, no puedo ir solo con cont
                while (cont != cantAntecedentes):
                    aux2.append(aux[cont2])
                    aux3.remove(aux[cont2])
                    if (cont2 != len(aux)):
                        cont2 = 0 #vuelve a la primer posicion
                    aux4.append(aux2) #antecedente
                    aux4.append(aux3) #consecuente
                    if confianzaMinima(transacciones, aux4, minConf):
                        regla.append(aux4[1])
                        regla.append(aux4[2])
                        reglas.append(regla)
                    cont += 1
                    cont2 += 1
            return reglas
'''
if __name__=="__main__":
    transacciones = [[1,2,3,4],[3,4],[2,4],[1,2],[1,2],[1,2,3,4]]
    #ff [[listaElementos], soporte] primer elemento 0 segundo 1
    #confianza = soportef/cantAntecedente
    #ff = [[1],4],[[2],5],[[3],3],[[4],4],[[1,2],4],[[1,3],2],[[1,4],2],[[2,3],2],[[2,4],3],[[3,4],3],[[1,2,3],2],[[1,2,4],2],[[1,3,4],2],[[2,3,4],2],[[1,2,3,4],2]]
    #ff = [[1,2],4],[[1,3],2],[[1,4],2],[[2,3],2],[[2,4],3],[[3,4],3]
    ff = [[1,2,3],2],[[1,2,4],2],[[1,3,4],2],[[2,3,4],2]
    #ff = [[[1,2,3,4],2],[[4,5,6,7],2]]
    minSup = 0.2
    minConf = 0.3*6
    r = genRules(transacciones, ff, minSup, minConf)
    #print (r)
