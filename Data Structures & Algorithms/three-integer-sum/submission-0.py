class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [] #initialize result
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:   
                if nums[left] + nums[right] == - nums[i]:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[left] + nums[right] > - nums[i]:
                    right -= 1
                else:
                    left += 1
        return result






#All the triplets.
#Triplets are distinct in index.
# Hash Map? 
# Any order for triplets
# 2 or 3 pointers?