class Solution:
    def reverseVowel(self,s:str) -> str:
        s = list(s)
        vowels = set('aeiouAEIOU')
        n = len(s)
        left = 0
        right = n-1
        while left < right :
            while left<right and s[left] not in vowels:
                left +=1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left],s[right] = s[right], s[left]
            left += 1
            right -= 1
            return  "".join(s)



if __name__ == '__main__':
    obj = Solution()
    res = obj.reverseVowel('AbCdeFGhIjKLOopneio')
    print(res)
