from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length  # Step 1: Initialize with 1's
        
        # Step 2: Prefix product
        prefix = 1
        for i in range(length):
            output[i] = prefix
            prefix *= nums[i]
        
        # Step 3: Postfix product
        postfix = 1
        for i in range(length - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output

# Example usage
nums = [1, 2, 3, 4]
sol = Solution()
print(sol.productExceptSelf(nums))  # [24, 12, 8, 6]

        