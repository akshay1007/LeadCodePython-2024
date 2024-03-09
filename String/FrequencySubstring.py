class FrequencySubstring:
    def __int__(self):
        text = None
        pat = None



    def freqCount(self,text,pat):
        len_text = len(text)
        len_pat = len(pat)
        res = 0

        for i in range(len_text - len_pat + 1):
            j = 0
            while (j < len_pat):
                if (text[i+j] != pat[j]):
                    break
                j +=1

            if(j == len_pat):
                res += 1
                j = 0
        print ('Total frequency match : ', res)



if __name__ == '__main__':
    text = 'ABABABABABBABABABABAAABABAB'
    pat = 'ABA'
    obj = FrequencySubstring()
    obj.freqCount(text,pat)