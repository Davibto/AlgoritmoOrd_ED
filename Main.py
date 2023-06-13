from Algoritmos import Algoritmos
from Menu import escolherAlgoritmo, lerArquivo
import time

#Arthur Ramón Souza Ferreira Martins - 20210027186
#Davi Baratto - 20210025940

lista = []

while True:
    try:
        opcao1 = int(input('\nEscolha qual arquivo será usado: \n1 - num.1000.1.in\n2 - num.1000.2.in\n3 - num.1000.3.in\n4 - num.1000.4.in\n5 - num.10000.1.in\n6 - num.10000.2.in\n7 - num.10000.3.in\n8 - num.10000.4.in\n9 - num.100000.1.in\n10 - num.100000.2.in\n11 - num.100000.3.in\n12 - num.100000.4.in\n13 - couting.txt\n0 - Sair\n'))
        
        if (opcao1 == 0):
            break

        if (opcao1 < 1 or opcao1 > 13):
            while(opcao1 < 0 or opcao1 > 13):
                 opcao1 = int(input('Opção inválida!\nEscolha qual arquivo será usado: \n1 - num.1000.1.in\n2 - num.1000.2.in\n3 - num.1000.3.in\n4 - num.1000.4.in\n5 - num.10000.1.in\n6 - num.10000.2.in\n7 - num.10000.3.in\n8 - num.10000.4.in\n9 - num.100000.1.in\n10 - num.100000.2.in\n11 - num.100000.3.in\n12 - num.100000.4.in\n13 - couting.txt\n0 - Sair\n'))
        
        lista = lerArquivo(opcao1)

        opcao2 = int(input('Escolha qual algoritmo sera utilizado: \n1 - SelectionSort\n2 - BubbleSort\n3 - InsertionSort\n4 - MergeSort\n5 - QuickSort\n6 - BogoSort\n7 - Comparar todos os tempos(menos BogoSort)\n0 - Sair\n'))
        
        if (opcao2 == 0):
            break

        if (opcao2 < 1 or opcao2 > 7):
            while(opcao2 < 0 or opcao2 > 7):
                 opcao2 = int(input('Escolha qual algoritmo sera utilizado: \n1 - SelectionSort\n2 - BubbleSort\n3 - InsertionSort\n4 - MergeSort\n5 - QuickSort\n6 - BogoSort\n7 - Comparar todos os tempos(menos BogoSort)\n0 - Sair\n'))
        
        escolherAlgoritmo(opcao2,lista)
                
    except ValueError:
        print('Selecione um número válido')

