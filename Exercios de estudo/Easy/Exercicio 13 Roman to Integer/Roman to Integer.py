s='LIII'
class Solution:
    def romanToInt(self, s: str) -> int:
        s_list=list(s)
        qtd_list=len(s_list)
        i=0
        for i in range(qtd_list):
            if "M" in s_list[i]:
                s_list[i] = 1000
            elif "D" in s_list[i]:
                s_list[i] = 500
            elif "C" in s_list[i]:
                if i + 1 < qtd_list and "D" == s_list[i + 1]:
                    s_list[i] = 400
                    s_list[i + 1] = ""
                elif i + 1 < qtd_list and "M" == s_list[i + 1]:
                    s_list[i] = 900
                    s_list[i + 1] = ""
                else:
                    s_list[i] = 100
            elif "L" in s_list[i]:
                s_list[i] = 50
            elif "X" in s_list[i]:
                if i + 1 < qtd_list and "L" == s_list[i + 1]:
                    s_list[i] = 40
                    s_list[i + 1] = ""
                elif i + 1 < qtd_list and "C" == s_list[i + 1]:
                    s_list[i] = 90
                    s_list[i + 1] = ""
                else:
                    s_list[i] = 10
            elif "V" == s_list[i]:
                s_list[i] = 5
            elif "I" == s_list[i]:
                if i+1 < qtd_list and "V" == s_list[i+1]:
                    s_list[i] = 4
                    s_list[i + 1] = ""
                elif i+1 < qtd_list and "X" == s_list[i+1]:
                    s_list[i] = 9
                    s_list[i + 1] = ""
                else:
                    s_list[i] = 1


        for i in range(qtd_list):
            if s_list[i] == "":
                s_list[i]=0
        return sum(s_list)





sol= Solution()
print(sol.romanToInt(s))
#print(sol.romanToInt(s))