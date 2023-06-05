import random

class Algoritmos:

    @staticmethod
    def selection_sort(lista):
        n = len(lista)
        for i in range(n-1):
            cont = i
            
            for j in range(i+1, n):
                if lista[j] < lista[cont]:
                    cont = j
            
            lista[i], lista[cont] = lista[cont], lista[i]
    
        return lista
    
    @staticmethod
    def bubble_sort(lista):
        n = len(lista)
    
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        
        return lista
    
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
        
        return lista
    
    @staticmethod
    def merge_sort(lista):
        if len(lista) <= 1:
            return lista
        
        # Divide o array
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]
        
        # Chama a função merge_sort recursivamente para as sublistas da esquerda e da direita
        esquerda = Algoritmos().merge_sort(esquerda)
        direita = Algoritmos().merge_sort(direita)
        
        # Combina as sublistas classificadas
        return Algoritmos().merge(esquerda, direita)

    @staticmethod
    def merge(esquerda, direita):
        resultado = []
        i = 0
        j = 0
        
        # Combina as sublistas ordenadamente
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
        
        # Adiciona os elementos restantes da sublista da esquerda, se houver
        while i < len(esquerda):
            resultado.append(esquerda[i])
            i += 1
        
        # Adiciona os elementos restantes da sublista da direita, se houver
        while j < len(direita):
            resultado.append(direita[j])
            j += 1
        
        return resultado
    
    @staticmethod
    def quick_sort(lista):

        if len(lista) <= 1:
            return lista
        
        meio = lista[len(lista) // 2]  
        menor = []
        igual = []
        maior = []
        
        for num in lista:
            if num < meio:
                menor.append(num)
            elif num == meio:
                igual.append(num)
            else:
                maior.append(num)
        
        return Algoritmos().quick_sort(menor) + igual + Algoritmos().quick_sort(maior)
    
    # BogoSort, feito pela brincadeira

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
        return lista

    
