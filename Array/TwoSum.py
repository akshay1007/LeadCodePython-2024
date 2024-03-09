from typing import List


class Solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return ([seen[target - num], i])
            elif num not in seen:
                seen[num] = i


if __name__ == '__main__':
    num = [2, 7, 11, 19]
    target = 9
    obj = Solution()
    res = obj.twosum(num, target)
    print(res)
