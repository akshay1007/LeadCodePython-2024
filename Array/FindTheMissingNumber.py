class Solution():
    def findMissingNum(self, arr):
        N = len(arr)
        total = (N+1)*(N+2)/2
        sum_of_arr = sum(arr)
        return total - sum_of_arr


if __name__ == '__main__':
    obj = Solution()
    arr = [1, 2, 4, 6, 3, 7, 8]
    print('Missing Number is : ', obj.findMissingNum(arr))
    max(arr)