class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for index1,num1 in enumerate(nums):
            product = 1
            for index2,num2 in enumerate(nums):
                if index2 == index1:
                    continue
                else:
                    product *= nums[index2]
            result.append(product)
            
        return result
        

        