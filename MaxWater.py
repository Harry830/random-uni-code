'''You are given an integer array heights where heights[i] represents the height of the i'th bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.'''
def maxArea(height):
        waters = []
        if len(height) <= 1 :
            return 0

        for counter_1 in range(len(height)):

            for counter_2 in range(len(height)):
                width = abs(counter_2-counter_1)
                if counter_1 == counter_2:
                    pass
                else:
                    if height[counter_1] > height[counter_2]:
                        length = height[counter_2]
                    else:
                        length = height[counter_1]
                    
                    area = length*width

                    waters.append(area)

        return max(waters)


print(maxArea([2]))

