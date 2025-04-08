
def answer(nums):
    count = 1
    
    for i in range(len(nums)-1):
        if nums[i+1]> nums[i]:
            count = count + 1
            # i = i+1
        # i = i+1  
    return count 
    


nums = [4,10,4,3,8,9]
ans = answer(nums)
print(ans)