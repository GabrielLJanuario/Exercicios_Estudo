from typing import List

class Inserir_dados:
    def __init__(self):
        self.nums = []

    def Inserindo_dados(self):
        self.nums = list(map(int, input("Digite os numeros para a lista: ").split()))

        self.target = int(input("Digite o valor de Terget: "))

class Solution():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indice_resultado = {}

        for i, num in enumerate(nums):
            valor = target - num
            if valor in indice_resultado:
                return [indice_resultado[valor], i]
            indice_resultado[num] = i

        return None

dados = Inserir_dados()

dados.Inserindo_dados()

resultado = Solution()

print(resultado.twoSum(dados.nums, dados.target))