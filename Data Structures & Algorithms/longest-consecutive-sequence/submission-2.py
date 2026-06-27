class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force
        longest = 0

        for num in nums:
            current_num = num
            current_length = 1

            while current_num + 1 in nums:
                current_num += 1
                current_length += 1

            longest = max(longest, current_length)

        return longest

        #sorting
        '''
        if not nums:
            return 0
        nums.sort()
        longest = 1
        current = 1
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                continue
            elif nums[i] == nums[i-1] + 1:
                current += 1
            else:
                current = 1
            longest = max(current, longest)
        return longest'''
        