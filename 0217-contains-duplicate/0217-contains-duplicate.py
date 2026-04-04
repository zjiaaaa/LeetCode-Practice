class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for i, num in enumerate(nums):
            if nums[i] in set1:
                return True
            set1.add(num)
        return False
        