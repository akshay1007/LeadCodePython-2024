# Simple python program to count
# occurrences of pat in txt.

class SubStringCount:
    def __int__(self):
        pass

    def sub_string_count(self, main_str, pattern):
        try:
            count = main_str.count(pattern)
            return count
        except Exception as e:
            raise e


    def countFreq(self,pat, txt):
        M = len(pat)
        N = len(txt)
        res = 0

        # A loop to slide pat[] one by one
        for i in range(N - M + 1):

            # For current index i, check
            # for pattern match
            j = 0
            while j < M:
                if (txt[i + j] != pat[j]):
                    break
                j += 1

            if (j == M):
                res += 1
                j = 0
        return res
# Driver Code
if __name__ == '__main__':
    input = 'dhimanman'
    pattern = 'man'
    obj = SubStringCount()
    res = obj.sub_string_count(input, pattern)
    print('Total number of occurance in string :', res)
