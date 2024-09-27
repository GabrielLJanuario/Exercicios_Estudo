from typing import List

from Tools.scripts.summarize_stats import print_title

strs=["flower","flow","flight"]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        list_prefixo=[]
        i=0
        j=0
        palavras=[list(strs) for strs in strs]
        menor_linha=min(palavras, key=len) # Encontrar a linha com o maior número de caracteres
        for i in range(len(palavras)):
            for j in range(len(menor_linha)):
                if palavras[i][j]==menor_linha[j]:
                    print()
                else:
                    break














sol= Solution()
sol.longestCommonPrefix(strs)
