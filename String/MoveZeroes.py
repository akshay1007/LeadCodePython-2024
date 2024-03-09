from typing import List


class Solution:
    def mozeZeroes(self, nums:List[int]) -> None:
      index = 0
      for i in range(len(nums)):
          if nums[i] != 0 :
              nums[i], nums[index]=  nums[index], nums[i]
              index += 1
      print(nums)
      return nums

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12,0,0,5,7,8,0,0]
    obj = Solution()
    res = obj.mozeZeroes(nums)
    print(res)


