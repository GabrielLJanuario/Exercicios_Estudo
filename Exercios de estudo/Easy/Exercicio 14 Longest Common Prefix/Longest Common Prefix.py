from typing import List, Counter

strs=["cir","car"]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        resposta=[]
        palavras=[list(strs) for strs in strs]
        menor_linha=min(palavras, key=len) # Encontrar a linha com o menor número de caracteres
        for i in range(len(menor_linha)):
            for j in range(len(palavras)):
                if palavras[j][i] != menor_linha[i]: # Verifica na menor lista se a letra que est no indice é igual a da lista palavras
                    return ''.join(resposta)
            resposta.append(menor_linha[i])


        return ''.join(resposta)



sol= Solution()
print(sol.longestCommonPrefix(strs))
