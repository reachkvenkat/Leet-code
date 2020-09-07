#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1, root2):
        lis = []
        curr1 = root1
        curr2 = root2
        
        def traverse(root, lis):
            
            if root.left is not None:
                lis = traverse(root.left, lis)
            
            if root.right is not None:
                lis = traverse(root.right, lis)
                
            lis.append(root.val)
            
            return lis
            
        if curr1 is not None:
            lis = traverse(curr1, lis)
        
        if curr2 is not None:
            lis = traverse(curr2, lis)
        
        lis.sort()
        
        return lis