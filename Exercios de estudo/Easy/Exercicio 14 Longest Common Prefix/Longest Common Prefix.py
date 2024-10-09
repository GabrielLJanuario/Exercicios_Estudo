from typing import List, Counter

strs=["cir","car"]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        resposta=[]
        palavras=[list(strs) for strs in strs]
        menor_linha=min(palavras, key=len) # Encontrar a linha com o menor número de caracteres
        for i in range(len(menor_linha)): # Percorre a quantidade de itens de menor linha
            for j in range(len(palavras)): #Percorre a quantidade de itens de palavras
                if palavras[j][i] != menor_linha[i]: # Verifica na menor lista se a letra que est no indice é igual a da lista palavras
                    return ''.join(resposta) # Retorna em txt a letra repetida da posição
            resposta.append(menor_linha[i]) # Adiciona na lista a resposta


        return ''.join(resposta) # Retorna a resposta do enunciado



sol= Solution()
print(sol.longestCommonPrefix(strs))
