class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #brute force
        '''for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False'''

        #optimised - tc: O(N) , space : O(N)
        look = set()
        for i in range(len(nums)):
            if nums[i] in look:
                return True
            look.add(nums[i])
        return False