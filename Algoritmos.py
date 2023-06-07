import random

class Algoritmos:

    @staticmethod
    def selection_sort(lista):
        n = len(lista)
        for i in range(n-1):
            cont = i
            
            for j in range(i, n):
                if lista[j] < lista[cont]:
                    cont = j
            
            if lista[i] > lista[cont]:
                aux = lista[i]
                lista [i] = lista[cont]
                lista[cont] = aux
    
    @staticmethod
    def bubble_sort(lista):
        n = len(lista)
    
        for i in range(n - 1):
            for j in range(n - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        
    @staticmethod
    def insertion_sort(lista):
        n = len(lista)

        for i in range(1, n):
            atual = lista[i]
            j = i - 1
            
            while j >= 0 and lista[j] > atual:
                lista[j + 1] = lista[j]
                j -= 1
            
            lista[j + 1] = atual
        
    @staticmethod
    def merge_sort(lista, inicio=0, fim=None):
        if fim is None:
            fim = len(lista)
            
        if((fim - inicio) > 1):
            meio = (fim + inicio) // 2
            Algoritmos.merge_sort(lista, inicio, meio)
            Algoritmos.merge_sort(lista, meio, fim)
            Algoritmos.merge(lista, inicio, meio, fim)

    @staticmethod
    def merge(lista, inicio, meio, fim):
        esquerda = lista[inicio:meio]
        direita = lista[meio:fim]
        top_esquerda = 0
        top_direita = 0

        for i in range(inicio, fim):
            if top_esquerda >= len(esquerda):
                lista[i] = direita[top_direita]
                top_direita = top_direita + 1

            elif top_direita >= len(direita):
                lista[i] = esquerda[top_esquerda]
                top_esquerda = top_esquerda + 1
                
            elif esquerda[top_esquerda] < direita[top_direita]:
                lista[i] = esquerda[top_esquerda]
                top_esquerda = top_esquerda + 1
            else:
                lista[i] = direita[top_direita]
                top_direita = top_direita + 1
    
    @staticmethod
    def quick_sort(lista, inicio=0, fim=None):
        if fim is None:
            fim = len(lista)-1
        if inicio < fim:
            p = Algoritmos.partition(lista, inicio, fim)
            Algoritmos.quick_sort(lista, inicio, p-1)
            Algoritmos.quick_sort(lista, p+1, fim)
        
    @staticmethod
    def partition(lista, inicio, fim):
        pivo = lista[fim]
        i = inicio
        for j in range(inicio, fim):
            if lista[j] <= pivo:
                lista[j], lista[i] = lista[i], lista[j]
                i = i + 1
        lista[i], lista[fim] = lista[fim], lista[i]
        return i

    @staticmethod
    def verificador(lista): #verifica se a lista esta ordenada
        n = len(lista)
        for i in range(1, n):
            if lista[i] < lista[i - 1]:
                return False
        return True

    @staticmethod
    def bogo_sort(lista):
        while not Algoritmos().verificador(lista): #se a lista não estiver ordenada embaralha aleatoriamente ela
            random.shuffle(lista)

    
