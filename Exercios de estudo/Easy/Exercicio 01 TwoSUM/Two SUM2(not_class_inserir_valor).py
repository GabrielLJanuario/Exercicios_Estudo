from typing import List
nums=[2,7,11,15]
target=9
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indice_resultado = {}

        for i, num in enumerate(nums):
            valor = target - num
            if valor in indice_resultado:
                return [indice_resultado[valor], i]
            indice_resultado[num] = i



sol= Solution()
print(sol.twoSum(nums,target))
