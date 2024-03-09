

class Solution:
    def gcdOfString(self,str1:str,str2:str)-> str:
        len1 , len2 = len(str1), len(str2)

        def isDivisior(l):
            if len1 % l or len2 % l:
                return False

            f1,f2 = len1 // l , len2 // l
            return str1[:l]*f1 == str1 and str1[:l]* f2 == str2

        for l in range(min(len1,len2),0,-1):
            if isDivisior(l):
                return str1[:l]
        return ""


if __name__ == '__main__':
    obj = Solution()
    str1 = "ABABAB"
    str2 = "ABAB"
    res = obj.gcdOfString(str1,str2)
    print(res)
