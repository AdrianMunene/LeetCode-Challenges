import operator
from operator import itemgetter
class Solution(object):
    def maxPoints(self, points):
        points = sorted(points, key = itemgetter(0))

