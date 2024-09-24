from typing import List

import self


class Inserir_dados:
    def __init__(self):
        self.nums = []

    def Inserindo_dados(self):
        self.nums = list(map(int, input("Digite os numeros para a lista: ").split()))

        self.target = int(input("Digite o valor de Terget: "))



class Solution():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indice_resultado = []

        for i, num in enumerate(nums):
            valor = num - target
            print(valor)

        return;

dados = Inserir_dados()

dados.Inserindo_dados()

resultado = Solution()

resultado.twoSum(dados.nums, dados.target)

print(resultado.twoSum(dados.nums, dados.target))