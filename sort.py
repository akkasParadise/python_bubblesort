




def bubblesort(nums):
    for _ in range(len(nums)):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                tmp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = tmp
                
    return nums
                

nums = [7,9,9,0,1,2,4,6,8,5]

hello = bubblesort(nums)
print(hello)
                
                
                
                
                








