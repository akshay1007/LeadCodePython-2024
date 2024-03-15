
class Solution:
    def freq(self,input:str, n:int):
        dic = {}
        for item in input:
            if item in dic:
                dic[item] += 1
            else :
                dic[item] = 1

        # get max value from dic
        max_value = max(list(dic.values()))
        if (n > max_value):
            return -1

        top_list = (list(dic.values()))
        print(top_list)

        # get all the keys matching to values
        while n>0:  # M(n)
            for key, value in dic.items():  # O(N)
                if value == max_value  or (value == max_value-n):
                    print(key)
            n -= 1

if __name__ == '__main__':
    input = ['Test', 'Bangalore', 'Mensa', 'Test', 'Hello', 'Bangalore', 'Test', 'Hello', 'Bangalore']
    obj = Solution()
    obj.freq(input,2)



