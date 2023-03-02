import operator
from operator import itemgetter
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #Sorts, 'points' a list of lists, by the value in the second[1] index in each list
        points = sorted(points, key = itemgetter(1))
        print(points)
        arrowcount = 1
        #Since 'points' is sorted according to the last index, points[0][1] is the value closest to x = 0 and points[-1][-1] is the value farthest from x = 0 for the given list
        #'pos' indicates the position of the arrow along the x - axis
        pos = points[0][1]

        for start, end in points:
            #Checks whether the position of the arrow is before the 'start' of the current list
            if pos < start:
                #If it is move the pos to the 'end' of the current list; increment arrowcount by 1
                pos = end
                arrowcount +=1
                #This allows the code to check whether one arrow is required 
                #for multiple consecutive ballons or multiple arrows for consecutive balloons because 
                #if the 'start' of the succeeding list is less than the 'end' of the preceeding list 
                #one balloon can be used to pop both of them
        return arrowcount

obj1 = Solution()
print(obj1.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))

                       
