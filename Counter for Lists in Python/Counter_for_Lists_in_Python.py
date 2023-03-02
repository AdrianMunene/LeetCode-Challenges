from collections import Counter
class Solution(object):
    def minimumRounds(self, tasks):

        n = 0
        count = Counter(tasks)
        for freq in count.values():
            if freq == 1:
                return -1
            elif (freq - 2) % 3 == 0:
                n += (freq - 2) // 3 + 1
            elif (freq - 4) % 3 == 0:
                n += (freq-4) // 3+2
            elif freq % 3 == 0:
                n += freq // 3
            else:
                n += freq //2

        return n

        