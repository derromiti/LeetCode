#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i, j]
        map = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if map.get(needed) is None:
                map[nums[i]] = i
            else:
                return [map.get(needed), i]


# @lc code=end
