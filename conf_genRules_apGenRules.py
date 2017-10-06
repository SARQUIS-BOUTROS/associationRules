def confianzaMinima (transacciones, itemsf, minConf):
    faux.append(itemsf[1])
    faux.extend(itemsf[2])#uno las dos partes asi me genera una sola lista con todos los elementos, itemsf es una lista de dos elementos, el antecedente y el consecuente
    fcont = 0 #contador f
    antcont = 0 #contador antecedente de itemsf o sea itemsf[1]
    for transaccion in transacciones:
        cont = 0 #renuevo por cada transaccion
        for item in aux:
            if item in transaccion:
                cont += 1 #voy sumando la cantidad de veces que coinciden los elementos en la transaccion individual
                if cont == len(faux): #si coinciden todos le sumo 1 ya que esos elementos aparecen en la transaccion
                    fcont += 1
            if item in itemsf[1]: #quiere decir que el item de f tambien es un antecedente
                antcont +=1
    confianza = fcont/antcont
    if confianza >= minConf:
        return True
    return False

def genRules (transacciones, itemsFrecuentes, minSup, minConf,k):
#la idea del codigo anterior es [1,2,3] toma primero el 1 lo agrega como consecuente y lo que queda de la lista es precedente, asi va haciendo en el bucle
    if k >= 2:
        reglas = []
        hh1 = []
        for f in itemsFrecuentes:
            regla = []
            aux = f
            aux2 = []
            for item in f:
                aux.remove(item)
                aux2.append([aux])
                aux2.append([item])
                if confianzaMinima(transacciones, aux2, minConf):#no se definio
                    regla.append(aux2[1])
                    regla.append(aux2[2])
                    hh1.append(item)
                    reglas.append(regla)
            reglas.extend(apGenRules(f, hh1, k, m = 1)) #concateno la lista de un elemento con la de mas de un elemento
    return reglas

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

if __name__=="__main__":
    transacciones = [[1,3],[1,4],[2,3,4],[1,2],[1]]
    itemsFrecuentes = [[1],[2],[3],[4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[1,2,3],[1,2,4],[1,3,4],[2,3,4],[1,2,3,4]]
    k=2
    minSup = 0.8
    minConf = 0.9*5
    print (genRules(transacciones, itemsFrecuentes, minSup, minConf, k))
