class MergeStringAlternately:
    def mergAlternately(self, word1: str, word2: str):
        i = 0
        j = 0
        ans = ""

        while i < len(word1) and j < len(word2):
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1

        while i < len(word1):
            ans += word1[i]
            i += 1

        while j < len(word2):
            ans += word2[j]
            j += 1

        return ans

    def mergeAlternate(self,word1,word2):
        ans = ""
        for i in range(max(len(word1),len(word2))):
            if i < len(word1) and i < len(word2):
                ans += word1[i]+word2[i]
            elif len(word1) > i >= len(word2):
                ans += word1[i]
            else :
                ans += word2[i]
        return  ans

    def bestSolution(self,word1,word2):
        ans = ""
        i = 0
        while i< len(word1) or i < len(word2):
            if i< len(word1):
                ans += word1[i]
            if i < len(word2):
                ans += word2[i]
            i += 1
        return ans


if __name__ == '__main__':
    obj = MergeStringAlternately()

    # input
    word1 = "abc"
    word2 = "pqr"
    expected = "apbqcr"
    res = obj.mergAlternately(word1,word2)
    if res == expected:
        print("Test Case 1 pass ",res)

    # input
    word1 = "abcd"
    word2 = "pq"
    expected = "apbqcd"
    res = obj.mergeAlternate(word1, word2)
    if res == expected:
        print("Test Case 2 pass ", res)

    # input
    word1 = "abcd"
    word2 = "pq"
    expected = "apbqcd"
    res = obj.bestSolution(word1, word2)
    if res == expected:
        print("Test Case 3 pass ", res)

