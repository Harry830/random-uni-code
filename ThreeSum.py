'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.'''

def Threesum(numbers):
 
        result = []
        result_sets = []
        for idx1 in range(len(numbers)):
            for idx2 in range(len(numbers)):
                for idx3 in range(len(numbers)):
                    if idx1 == idx2 or idx2 == idx3 or idx3 == idx1:
                        pass
                    else:
                        if numbers[idx1] + numbers[idx2] + numbers[idx3] == 0:
                            if {numbers[idx1], numbers[idx2], numbers[idx3]} in result_sets:
                                pass
                            else:
                                result_sets.append({numbers[idx1], numbers[idx2], numbers[idx3]})
                                result.append([numbers[idx1], numbers[idx2], numbers[idx3]])
                                
        return result     
                         
print(Threesum([-1,0,1,2,-1,-4]))