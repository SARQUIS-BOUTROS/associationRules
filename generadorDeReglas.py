import itertools
def findsubsets(S,m):
    #print set(itertools.combinations(S, m)) #sacar
    return set(itertools.combinations(S, m))
def genRules (frequent_itemsets, confidence,D):
    s = []
    r = []
    length = 0
    count = 1
    inc1 = 0
    inc2 = 0
    num = 1
    m = []
    L= frequent_itemsets
    print L
    print "---------------------ASSOCIATION RULES------------------"
    print "RULES \t SUPPORT \t CONFIDENCE"
    print "--------------------------------------------------------"
    for list in L:
        for l in list:
            length = len(l)
            count = 1
            while count < length:
                s = []
                r = findsubsets(l,count)
                count += 1
                for item in r:
                    inc1 = 0
                    inc2 = 0
                    s = []
                    m = []
                    for i in item:
                        s.append(i)
                    for T in D:
                        if set(s).issubset(set(T)) == True:
                            inc1 += 1
                        if set(l).issubset(set(T)) == True:
                            inc2 += 1
                    if 100*inc2/inc1 >= confidence:
                        for index in l:
                            if index not in s:
                                m.append(index)
                        print "Rule#  %d : %s ==> %s %d %d" %(num, s, m, 100*inc2/len(D), 100*inc2/inc1)
                        num += 1

if __name__=="__main__":

    ff=[]
    ff1=[]
    ff2=[]
    ff.append(['1','3'])
    ff.append(['1','2'])
    ff.append(['1', '4'])
    ff.append (['3','4'])
    ff.append (['2', '3'])
    ff.append(['2','4'])
    lista=[]
    lista.append(ff)
    ff1.append (['1','3','4'])
    ff1.append (['1','2','3'])
    ff1.append(['1','2','4'])
    ff1.append (['2','3','4'])
    lista.append (ff1)
    ff2.append(['1','2','3','4'])
    lista.append(ff2)
    #print lista

    #fftoadas=[[1, 3], [1, 2], [1, 4], [3, 4], [2, 3], [2, 4], [1, 3, 4], [1, 2, 3],
     #[1, 2, 4], [2, 3, 4], [1, 2, 3, 4]]

transacciones = open('simpledat-sin-coma.txt', 'r') #lee el archivo
allTransac = []
for linea in transacciones.readlines():#lee linea por linea el archivo
    transac = linea.split() #me transforma el string linea en una lista
    transac = map(str,transac) #mapea de letras a numeros (para string no deberia usarse)
    transac.sort() #ordena la lista
    allTransac.append(transac) #agrega a la lista de todas las transacciones
print allTransac

     #lista son los ff que se generaron con 30% de confianza y 30% de soporte. a genRules le envio 30 que es de la confianza, 
     #no es necesario pasarle el soporte
r = genRules(lista, 30, allTransac)
print (r)
