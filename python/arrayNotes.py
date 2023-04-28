

class LeftRightSum(object):
    #find sum of values to the left and right of indexed value
    def sumFunction(self,nums):
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

    def itterativeFunction(self,nums):
        leftSum=0
        rightSum=0

        for idx, num in enumerate(nums):
            #calculate left sum
            for i in range(0,idx):
                leftSum+=nums[i]
            #calculate right sum
            for i in range(idx+1,len(nums)):
                rightSum+=nums[i]
            
            print(f"left sum: {leftSum} right sum {rightSum}")

    def fullSum(self,nums):
        ans=[]
        totalSum=sum(nums)
        leftSum=0
        rightSum=0

        for idx, num in enumerate(nums):
            if idx==0:
                rightSum=totalSum-num
            else:
                rightSum-=num
                leftSum+=nums[idx]
            print(f"idx{idx} left sum: {leftSum} right sum {rightSum}")


        #return ans        







nums=[1,2,3,4,5,6]
solution=LeftRightSum()
#solution.sumFunction(nums)
#solution.itterativeFunction(nums)
solution.fullSum(nums)