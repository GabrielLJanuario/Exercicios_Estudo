from typing import List
nums=[2,7,11,15]
target=9
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indice_resultado = []

        for i, num1 in enumerate(nums):
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                valor = num1 + num2
                if valor == target:
                    return [i, j]
        return indice_resultado;


sol= Solution()
print(sol.twoSum(nums,target))
