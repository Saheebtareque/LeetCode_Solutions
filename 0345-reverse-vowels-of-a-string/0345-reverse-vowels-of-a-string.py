class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a':1 , 'e':1, 'i':1, 'o':1, 'u':1, 'A':1 , 'E':1, 'I':1, 'O':1, 'U':1 }
        l,r = 0,len(s)-1
        p = list(s)
        while l<r :
            if p[l] not in vowels and p[r] not in vowels:
                l +=1
                r -=1
            elif p[l] not in vowels:
                l +=1
            elif p[r] not in vowels:
                r -=1
            else:
                p[l],p[r] = p[r],p[l]
                l += 1
                r -=1
        x = ''.join(p)
        return x


        