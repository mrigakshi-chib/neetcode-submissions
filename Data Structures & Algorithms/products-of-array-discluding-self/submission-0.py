class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        arr_prod = [1]*n
        for i in range(n):
            product = 1
            for j in range(n):
                if i!= j:
                    product *= nums[j]
            arr_prod[i] = product
        return arr_prod
        
        

        