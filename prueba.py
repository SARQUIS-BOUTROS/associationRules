import sys
from optparse import OptionParser

def leerDocumento(archivo):
    transacciones = open(archivo, 'r')#lee el archivo
    allTransac = []
    for linea in transacciones.readlines():#lee linea por linea el archivo
        transac = linea.split() #me transforma el string linea en una lista
        transac.sort() #ordena la lista
        allTransac.append(transac) #agrega a la lista de todas las transacciones
    return allTransac


if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option('-d', '--dataSet', dest='input', help='Dataset a analizar')
    (options, args) = parser.parse_args()

    if options.input is None:
        print 'No se especifico ningun dataset. Cerrando...\n'
        sys.exit('Cierre.')
    elif options.input is not None:
        listaTransacciones = leerDocumento(options.input)
    else:
        print 'Error de sistema.\n'
        sys.exit('Cierre.')

print(listaTransacciones)
