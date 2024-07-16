class Solution:
    def sum_n(self, n):
        if n<= 0 :
            return 0
        return n+ self.sum_n(n-1)

    def pairSumSequence(self,n):
        sum = 0
        for i in range(n):
            sum += self.pairSum(i,i+1)
        return sum

    def pairSum(self, a, b):
        return a+b



if __name__ == '__main__':
    obj = Solution()
    n = 1000000
    print('Sum of ',n, 'is : ', obj.pairSumSequence(n))