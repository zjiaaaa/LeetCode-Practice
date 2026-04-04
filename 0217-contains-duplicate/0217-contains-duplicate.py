class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic ={}
        for i, num in enumerate(nums):
            if nums[i] in dic:
                return True
            dic[num] = i
        return False
        