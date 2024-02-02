class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        global z
        z = -1
        for i in range(len(word)):
            if word[i] == ch:
                z = i
                break
            else:
                continue
        if z == -1:
            return word
        q = z+1
        tempString = word[:q]
        str3 = tempString[::-1]
        string2 = word[q:]
        final = ''
        final = str3 + string2
        return final
        