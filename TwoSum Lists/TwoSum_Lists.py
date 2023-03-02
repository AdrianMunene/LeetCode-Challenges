#Attempt 1 at LeetCode Two Sums Challenge with time complexity O(n)
#Only works when the numbers are next to each other in the list  
"""class Solution(object):
    def twoSum(self, nums, target):

        matchlst = []
        n=1
        for i in range(len(nums)):
            if nums[i] + nums[n] == target:
                matchlst [0:1] = i , n
            else:
                n+=1

        return matchlst[0:2]

target = 6
nums = [3,2]
matchlst = []
n = 1
for i in range(len(nums)):
    if nums[i] + nums[n] == target:
        matchlst [0:1] = i, n
        break
    else:
        n+=1

print(str(matchlst[0:2]))
"""    
#Attempt 2 at LeetCode Challenge. Time Complexity O(n)
"""
target = 6
nums = [3,2,3]
matchlst = []
diff = 0
n = 0 
for i in range(len(nums)*len(nums)):
    if i % len(nums) == 0:
        n = 0
    else:
        n+=1
"""
#Attempt 3 Uisng Modulus Succesfully
def is_array_sorted(arr):
  for i in range(len(arr)):
    if arr[i] <= arr[i-1] or arr[i] <= arr[(i+1) % len(arr)]:
      return False
  return True

arr = [1, 2, 3, 4, 5]
print(is_array_sorted(arr)) # True
arr = [1, 3, 2, 4, 5]
print(is_array_sorted(arr)) # False
"""
def is_array_sorted(arr):
  for i in range(len(arr)):
    if arr[i] <= arr[i % len(arr)]:
      return False
  return True

arr = [1, 2, 3, 4, 5]
print(is_array_sorted(arr)) # True
arr =
"""
        
    
    
    
    
    

