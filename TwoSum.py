def twoSum(numbers,target):
        for currPos  in range(len(numbers)):
            for currIdx in range(len(numbers)):
                if currPos == currIdx:
                      pass
                else:
                    if numbers[currPos] + numbers[currIdx] == target:
                         return [currPos+1,currIdx+1]
                    
                         
print(twoSum([1,2,3,4],3))