#Adrian Munene Bikuri
#01/01/2023
#LeetCode Challlenge Word_Pattern
class Solution(object):
    def wordPattern(self, pattern, s):

        #Variable to store boolean return
        b = 0
        
        #Arbitrary name for empty dictionaries
        maps = {}

        #Empty list used to reconstruct string using the dictionary
        s1 = []

        if (len(pattern) >= 1 and len(pattern) <= 300) and (len(s) >= 1 and len(s)<=3000):

            #This splits the sentence, s, along the white spaces and returns a list of strings
            s = s.split()
            
            if(len(pattern) == len(s)):
                for i in range(len(pattern)):
                    maps.setdefault(pattern[i], s[i])

            #Exits execution if length of pattern is not equal to length of s.split()
            else:
                return False

            #Reconstructs the sentence into 's1' from the dictionary
            for j in range(len(pattern)):
                s1.insert(j, maps[pattern[j]])

            #Checks if there are any repeated values in dictionary, if there are, b is set to false as the dictionary would reconstruct the string s verbatim if there are repeating values giving an incorrect result
            if len(maps.values()) != len(set(maps.values())):
                   b = False
            else:
                 b = s1 == s

        else:
            return 1

        return b 








