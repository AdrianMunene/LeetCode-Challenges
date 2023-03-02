#Adrian Munene Bikuri
#02/01/2023
#LeetCode Challenge Detect_Capital
class Solution(object):
    def detectCapitalUse(self, word):

        #Variable to store rtype: bool
        b = 0

        if len(word)>= 1 and len(word) <=100:
            
            if len(word) == 1:
                b = True
                return b

            if word.istitle() == True or word.isupper() == True or word.islower() == True:
                b = True
            else:
                b = False

        else:
            b = False

        return b

obj1 = Solution()
print(obj1.detectCapitalUse('FFFFFFFFf'))

