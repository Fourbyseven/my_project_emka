# Задачи про видео №1




class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ''
        
        i = 0
        while True:
            try:
                symb = strs[0][i]
            except:
                return res
            for word in strs:
                try:
                    if word[i]!=symb:
                        return res
                except:
                    return res
            res += symb
            i+=1
        return res


# Задачи по видео № 2

