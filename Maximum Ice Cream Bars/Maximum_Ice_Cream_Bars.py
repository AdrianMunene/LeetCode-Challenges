#Adrian Munene Bikuri
#08/01/2023
#LeetCode Challenge Maximum Ice Cream Bar - Medium
#Fastest solved medium level challenge :)
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        icecreams = 0
        for i in costs:
            if i <= coins:
                icecreams += 1
                coins = coins - i


        return icecreams

obj1 = Solution()
print(obj1.maxIceCream(costs = [27,23,33,26,46,86,70,85,89,82,57,66,42,18,18,5,46,56,42,82,52,78,4,27,96,74,74,52,2,24,78,18,42,10,12,10,80,30,60,38,32,7,98,26,18,62,50,42,15,14,32,86,93,98,47,46,58,42,74,69,51,53,58,40,66,46,65,2,10,82,94,26,6,78,2,101,97,16,12,18,71,5,46,22,58,12,18,62,61,51,2,18,34,12,36,58,20,12,17,70], coins = 241))