class Solution:
    # Two pointer
    def reverseWords(self,s:str)-> str:
        s = s.split()
        left = 0
        right = len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left +=1
            right -=1

        return ' '.join(s).strip()

    def reverseWords_best(self,s:str)->str:
        s = s.strip()
        l = s.split()
        m = l[::-1]
        return ' '.join(m)

if __name__ == '__main__':
    obj = Solution()
    input = "the sky is blue"
    expectd  = "blue is sky the"
    res = obj.reverseWords(input)
    if res == expectd:
        print('Test Case 1 pass : output -> ',res )
    input = "  hello world       "
    expectd = "world hello"
    res = obj.reverseWords(input)
    if res == expectd:
        print('Test Case 2 pass : output -> ',res )

    input = "the sky is blue"
    expectd = "blue is sky the"
    res = obj.reverseWords(input)
    if res == expectd:
        print('Test Case 3 pass : output -> ', res)
    input = "  hello world       "
    expectd = "world hello"
    res = obj.reverseWords_best(input)
    if res == expectd:
        print('Test Case 4 pass : output -> ', res)
