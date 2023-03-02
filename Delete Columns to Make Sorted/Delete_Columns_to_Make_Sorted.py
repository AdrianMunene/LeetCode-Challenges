#Adrian Munene Bikuri
#03/01/2023
#LeetCode Challenge Delete_Column_To_Make_Sorted
class Solution(object):
    def minDeletionSize(self, strs):
        
        #rtype: int
        cnt = 0

        clmns = []
        
        k = 0
        l = 0
        #Loop re-arranges the input list to create a list of columns
        #Range is len(strs) * len(strs[0]) because that's the number of letters in the input list
        for i in range(len(strs) * len(strs[0])):
            clmns.append(strs[k][l])
            k += 1
            #Returns k to 0 when condition is met and adds a white space to separate the columns
            if k >= len(strs):
                k = 0
                l += 1
                clmns.append(' ')
            #Breaks out of for loop when condition is met as all letters have been re-arranged
            #Use of this ensures loop doesn't go out of index string range
            if l >= len(strs[0]):
                break
        #Joins the multiple list elements with a blank space and splits at the white space to return a list of the columns
        clmns = ''.join(clmns).split()

        #Checks if each column is sorted alphabetically and adds 1 to count for every column not alphabetic
        for j in range(len(clmns)):
            if list(clmns[j]) != sorted(clmns[j]):
                cnt += 1
        print(cnt)
        return cnt

obj1 = Solution()
obj1.minDeletionSize(['abc', 'def', 'ghi', 'jkl'])