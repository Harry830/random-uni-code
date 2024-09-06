def longestConsecutive(nums):
    if len(nums) ==0:
            return 0
    elif len(nums) ==1:
            return 1
    nums = list(set(nums))
    nums.sort()
    maxLen = []
    curr = [nums[0]]
    
    for num in nums[1:]:
        if num == curr[-1]+1:
            curr.append(num)
            if len(maxLen) < len(curr):
                maxLen = curr.copy()
        else:
            curr = [num]
        
    return len(maxLen)

print(longestConsecutive([2,20,4,10,3,4,5]))