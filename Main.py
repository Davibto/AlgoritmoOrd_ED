from Algoritmos import Algoritmos
import time


arquivo = "instancias-num/num.100000.4.in"

lista = []

with open(arquivo, 'r') as arquivo:
    arq = arquivo.readlines()

for linha in arq:
    num = int(linha)
    lista.append(num)

opcao = input("Escolha qual algoritmo sera utilizado: \n1 - SelectionSort\n2 - BubbleSort\n3 - InsertionSort\n4 - MergeSort\n5 - QuickSort\n6 - BogoSort\n0 - Sair\n")

while(opcao != '0'):
    if opcao == '1':
        ini = time.time()
        Algoritmos().selection_sort(lista)
        fim = time.time()
        tempo_total = fim - ini
        print("Tempo total:", tempo_total, "segundos")      
        break

    elif opcao == '2':
        ini = time.time()
        Algoritmos().bubble_sort(lista)
        fim = time.time()
        tempo_total = fim - ini
        print("Tempo total:", tempo_total, "segundos")     
        break

    elif opcao == '3':
        ini = time.time()
        Algoritmos().insertion_sort(lista)
        fim = time.time()
        tempo_total = fim - ini
        print("Tempo total:", tempo_total, "segundos")      
        break

    elif opcao == '4':
        ini = time.time()
        Algoritmos().merge_sort(lista)
        fim = time.time()
        tempo_total = fim - ini
        print("Tempo total:", tempo_total, "segundos")     
        break

    elif opcao == '5':
        ini = time.time()
        Algoritmos().quick_sort(lista)
        fim = time.time()
        tempo_total = fim - ini
        print("Tempo total:", tempo_total, "segundos")      
        break

    elif opcao == '6':
        ini = time.time()
        Algoritmos().bogo_sort(lista)
        fim = time.time()
        tempo_total = fim - ini
        print("Tempo total:", tempo_total, "segundos")
        break

    else:
        print("Opcao invalida")
        break



