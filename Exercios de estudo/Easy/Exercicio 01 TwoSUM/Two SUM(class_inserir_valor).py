from typing import List

class Inserir_dados:

    def __init__(self): #Função que cria uma lista.
        self.nums = []


    def Inserindo_dados(self): #Função que serve para inderir os itens da lista e o numero Target.
        self.nums = list(map(int, input("Digite os numeros para a lista: ").split()))

        self.target = int(input("Digite o valor de Terget: "))


#Classe para verificar se na lista os numeros que se somando dão o valor de Target e irão retornar os indices .class Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indice_resultado = {} #Dicionario que é usado para ser posto o resultado dos indices (usado por otimizar).


        for i, num in enumerate(nums): # Esse FOR ele passa pelos indices e verificar se o (Target-Valor[indice])...
            valor = target - num       # ... da um valor presente na lista, e adiciona os indices no Dicionario.
            if valor in indice_resultado:
                return [indice_resultado[valor], i]
            indice_resultado[num] = i

        return None

dados = Inserir_dados()

dados.Inserindo_dados()



resultado = Solution()

print(resultado.twoSum(dados.nums, dados.target))