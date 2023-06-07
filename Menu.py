
import time
from Algoritmos import Algoritmos

def lerArquivo(opcao):
    lista = []
    
    if opcao == '1':
        arquivo = "instancias-num/num.1000.1.in"
    elif opcao == '2':
        arquivo = "instancias-num/num.1000.2.in"
    elif opcao == '3':
        arquivo = "instancias-num/num.1000.3.in"
    elif opcao == '4':
        arquivo = "instancias-num/num.1000.4.in"
    elif opcao == '5':
        arquivo = "instancias-num/num.10000.1.in"
    elif opcao == '6':
        arquivo = "instancias-num/num.10000.2.in"
    elif opcao == '7':
        arquivo = "instancias-num/num.10000.3.in"
    elif opcao == '8':
        arquivo = "instancias-num/num.10000.4.in"
    elif opcao == '9':
        arquivo = "instancias-num/num.100000.1.in"
    elif opcao == '10':
        arquivo = "instancias-num/num.100000.2.in"
    elif opcao == '11':
        arquivo = "instancias-num/num.100000.3.in"
    elif opcao == '12':
        arquivo = "instancias-num/num.100000.4.in"
    else:
        print("Opção inválida!")

    with open(arquivo, 'r') as arquivo:
        arq = arquivo.readlines()

    for linha in arq:
        num = int(linha)
        lista.append(num)

    return lista

def escolherAlgoritmo(opcao,lista):
    if opcao == '1':
        l1 = lista.copy()
        ini = time.time()
        Algoritmos().selection_sort(l1)
        fim = time.time()
        tempo_total = fim - ini
        print("Tempo total SelectionSort:", tempo_total, "segundos")
        print(l1,'\n')

    elif opcao == '2':
        l2 = lista.copy()
        ini = time.time()
        Algoritmos().bubble_sort(l2)
        fim = time.time()
        tempo_total = fim - ini
        print("Tempo total BubbleSort:", tempo_total, "segundos")
        print(l2,'\n')

    elif opcao == '3':
        l3 = lista.copy()
        ini = time.time()
        Algoritmos().insertion_sort(l3)
        fim = time.time()
        tempo_total = fim - ini
        print("Tempo total InsertionSort:", tempo_total, "segundos")
        print(l3,'\n')

    elif opcao == '4':
        l4 = lista.copy()
        ini = time.time()
        Algoritmos().merge_sort(l4)
        fim = time.time()
        tempo_total = fim - ini
        print("Tempo total MergeSort:", tempo_total, "segundos")
        print(l4,'\n')

    elif opcao == '5':
        l5 = lista.copy()
        ini = time.time()
        Algoritmos().quick_sort(l5)
        fim = time.time()
        tempo_total = fim - ini
        print("Tempo total QuickSort:", tempo_total, "segundos")
        print(l5,'\n')

    elif opcao == '6':
        l6 = lista.copy()
        ini = time.time()
        Algoritmos().bogo_sort(l6)
        fim = time.time()
        tempo_total = fim - ini
        print("Tempo total BogoSort:", tempo_total, "segundos")
        print(l6,'\n')
    
    elif opcao == '7':
        escolherAlgoritmo('1',lista)
        escolherAlgoritmo('2',lista)
        escolherAlgoritmo('3',lista)
        escolherAlgoritmo('4',lista)
        escolherAlgoritmo('5',lista)      

    else:
        print("Opcao invalida!")