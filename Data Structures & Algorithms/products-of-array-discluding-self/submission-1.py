class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''brute force
        n = len(nums)
        arr_prod = [1]*n
        for i in range(n):
            product = 1
            for j in range(n):
                if i!= j:
                    product *= nums[j]
            arr_prod[i] = product
        return arr_prod '''

        n = len(nums)
        left_arr = [1] * n
        right_arr = [1] * n
        final_prod = [1] *n
        for i in range(1,n):
            left_arr[i] = left_arr[i-1] * nums[i-1]
        for j in range(n-2, -1,-1):
            right_arr[j] = right_arr[j + 1] * nums[j + 1]
        for i in range(n):
            final_prod[i] = left_arr[i] * right_arr[i]

        return final_prod
        
        

        