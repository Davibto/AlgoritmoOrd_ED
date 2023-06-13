import random

class Algoritmos:

    @staticmethod
    def selection_sort(lista):
        n = len(lista) #pega o tamanho da lista
        for i in range(n-1):
            cont = i #variavel que vai guardar o indice do menor elemento
            
            for j in range(i, n):
                if lista[j] < lista[cont]: #se o elemento atual for menor que o menor elemento
                    cont = j #atualiza o indice com o novo menor elemento
            
            #troca o menor elemento com o primeiro elemento
            if lista[i] > lista[cont]:
                aux = lista[i] #variavel auxiliar para guardar o elemento atual
                lista [i] = lista[cont] #troca o elemento atual com o menor elemento
                lista[cont] = aux #troca o menor elemento com o elemento atual
    
    @staticmethod
    def bubble_sort(lista):
        n = len(lista) #pega o tamanho da lista
    
        for i in range(n - 1): 
            for j in range(n - 1): #percorre a lista até o penultimo elemento
                if lista[j] > lista[j + 1]: #compara dois elementos adjacentes da lista
                    lista[j], lista[j + 1] = lista[j + 1], lista[j] # troca suas posições se o elemmento atual é maior que o proximo elemento
        
    @staticmethod
    def insertion_sort(lista):
        n = len(lista) #pega o tamanho da lista

        #Realiza uma comparação em ordem reversa com os elementos anteriores e move os elementos maiores para a direita
        for i in range(1, n):
            atual = lista[i]
            j = i - 1
            
            while j >= 0 and lista[j] > atual:
                lista[j + 1] = lista[j]
                j -= 1
            # Insere o elemento atual na posição correta
            lista[j + 1] = atual
        
    @staticmethod
    def merge_sort(lista, inicio=0, fim=None):
        if fim is None:  #verifica se a lista tem um fim, caso contrário, define o fim como o tamanho da lista
            fim = len(lista)
            
        if((fim - inicio) > 1):
            meio = (fim + inicio) // 2 #calcula o meio da lista
            Algoritmos.merge_sort(lista, inicio, meio) #chama recursivamente o merge_sort para a primeira metade da lista
            Algoritmos.merge_sort(lista, meio, fim) #chama recursivamente o merge_sort para a segunda metade da lista
            Algoritmos.merge(lista, inicio, meio, fim)  #fusão (merge) entre as duas metades da lista

    @staticmethod
    def merge(lista, inicio, meio, fim):
         #divide a lista em duas partes
        esquerda = lista[inicio:meio]
        direita = lista[meio:fim]
        top_esquerda = 0 #variavel que vai percorrer a lista da esquerda
        top_direita = 0 #variavel que vai percorrer a lista da direita

        # Combinar as sublistas esquerda e direita em ordem crescente
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
        if inicio < fim: #verifica se o índice de início é menor do que o índice de fim.
            p = Algoritmos.partition(lista, inicio, fim) #encontrar o pivô e particiona a lista
            Algoritmos.quick_sort(lista, inicio, p-1) #ordenar a parte da lista à esquerda do pivô.
            Algoritmos.quick_sort(lista, p+1, fim) #ordenar a parte da lista à direita do pivô.
        
    @staticmethod
    def partition(lista, inicio, fim):
        pivo = lista[fim] #define o pivo como o ultimo elemento da lista
        i = inicio #define o indice i como o inicio da lista
        for j in range(inicio, fim):
            if lista[j] <= pivo:
                lista[j], lista[i] = lista[i], lista[j] #troca o elemento atual com o elemento do indice i se o elemento atual for menor ou igual o pivo
                i = i + 1 #incrementa o indice i
        lista[i], lista[fim] = lista[fim], lista[i] #troca o elemento do indice i com o pivo
        return i

    @staticmethod
    def verificador(lista): #verifica se a lista esta ordenada
        n = len(lista) #pega o tamanho da lista
        for i in range(1, n):
            if lista[i] < lista[i - 1]: #se o elemento atual for menor que o elemento anterior retorna falso
                return False
        return True

    @staticmethod
    def bogo_sort(lista):
        while not Algoritmos().verificador(lista): #se a lista não estiver ordenada embaralha aleatoriamente ela
            random.shuffle(lista)