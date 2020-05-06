class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_num=None
        count=0
        for num in nums:
            if count==0:
                majority_num=num
            if majority_num==num:
                count+=1
            else:
                count-=1
        return majority_num