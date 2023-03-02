# Definition for a binary tree node.

#This class is a constructor
#When you create an object 'node' it sets attributes 'val=0', 'left=None', 'right=None' 
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


#Recursively traverses a binary tree in pre-order when given the root node
class Solution(object):
    def preorderTraversal(self, root):

        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        output = []
        if root: 
            output.append(root.val)

            output = output + self.preorderTraversal(root.left)

            output = output + self.preorderTraversal(root.right)

        return output
                                                     




root = TreeNode()
a1 = TreeNode()
a2 = TreeNode()
root.val = 0
a1.val = None
a2.val = 2
root.left = a1
root.right = a2
trvrse = Solution()
print(trvrse.preorderTraversal(root))
