from Algoritmos import Algoritmos
from Menu import escolherAlgoritmo, lerArquivo
import time


lista = []

opcao1 = input('Escolha qual arquivo será usado: \n1 - num.1000.1.in\n2 - num.1000.2.in\n3 - num.1000.3.in\n4 - num.1000.4.in\n5 - num.10000.1.in\n6 - num.10000.2.in\n7 - num.10000.3.in\n8 - num.10000.4.in\n9 - num.100000.1.in\n10 - num.100000.2.in\n11 - num.100000.3.in\n12 - num.100000.4.in\n0 - Sair\n')
lista = lerArquivo(opcao1)



opcao2 = input("Escolha qual algoritmo sera utilizado: \n1 - SelectionSort\n2 - BubbleSort\n3 - InsertionSort\n4 - MergeSort\n5 - QuickSort\n6 - BogoSort\n7 - Comparar todos os tempos(menos BogoSort)\n0 - Sair\n")
escolherAlgoritmo(opcao2,lista)



