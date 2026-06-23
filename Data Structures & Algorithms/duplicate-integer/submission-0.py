class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ''' brute force'''
        '''for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False'''

        '''optimised approach'''
        
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen[num] = i
        return False
        