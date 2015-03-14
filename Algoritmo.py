## Curso: Analisis de Algoritmos
## Tarea #2
## Profesor: Mauricio Rojas
## Alumna: Miuyin Yong Wong
## Carnet: 2014079293

## Caso base: cuando hay 2 elementos
## Se asume que la lista esta compuesta de numeros enteros y pares

lista_original = []

def tarea2(alist): 
    lista_original = alist[:]
    mergeSort(alist) 
    max_one = alist[len(alist)-1]
    max_two = alist[len(alist)-2]
    index_one = alist.index(max_one)
    index_two = alist.index(max_two)
    resultado_final = "La lista creada es: " + str(lista_original) + "\nEl indice del primer numero mayor es: "+ str(index_one)+ "\nEl indice del segundo numero mayor es: "+ str(index_two)
    return resultado_final

    
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def crearLista(longitud):
    i = 0
    alist = []
    while i < longitud:
        digito = int(input("Digite el " + str(i) + " digito de la lista: "))
        alist.append(digito)
        i+=1
    return alist
            
###################################################
##            Programa Principa                  ##
###################################################
print ("TAREA #2 - Analisis de lenguajes - Miuyin Yong Wong")
print ("---------------------------------------------------")
longitud = int(input("Digite la longitud de la lista que desea crear: "))
alist = crearLista(longitud)   
print(tarea2(alist))


