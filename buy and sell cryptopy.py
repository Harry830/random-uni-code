# prices = [10,1,5,6,7,1]

def maxProfit(prices):
        lengths = []
        # prices = prices[::-1]
        for test_num in range(len(prices)):

            for cur_num in prices[test_num+1:]:
                curr_len = cur_num - prices[test_num]
                lengths.append(curr_len)

        if max(lengths) <0:
            return 0
        else:
            return max(lengths) 












print(maxProfit([10,4,3,2,1]))