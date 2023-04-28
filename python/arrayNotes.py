

class Solution(object):
    #find sum of values to the left and right of indexed value
    def leftrightSum(self,nums):
        leftSum=0
        rightSum=0

        #using sum function
        ans=[]
        for i in range(len(nums)):
            leftSum=sum(nums[0:i])
            rightSum=sum(nums[i+1:])
            tempVal=f"[{leftSum},{rightSum}]"
            #print(type(tempVal))
            ans.append[(tempVal)]
        
        #return ans






nums=[1,2,3,4,5,6]
solution=Solution()
solution.leftrightSum(nums)
