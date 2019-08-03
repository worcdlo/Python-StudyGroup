# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:37:15 2019
HW9_Algorithm_Symmetric_Tree.py
@author: Aaron
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    

def isSymRecursive(root):
    if root == None:
        return True
    return compare_recursive([root], [root])


def compare_recursive(left_lt, right_lt):
    if len(left_lt) == 0:
        return True
    else:
        lnode = left_lt.pop(0)
        rnode = right_lt.pop(0)
        
        if lnode.val != rnode.val:
            return False
        else:
            if lnode.left != None and rnode.right != None:
                left_lt.append(lnode.left)
                right_lt.append(rnode.right)
            elif lnode.left != None or rnode.right != None:
                return False
            
            if lnode.right != None and rnode.left != None:
                left_lt.append(lnode.right)
                right_lt.append(rnode.left)
            elif lnode.right != None or rnode.left != None:
                return False
                
    return compare_recursive(left_lt, right_lt)


def isSymIterative(root):
    if root == None:
        return True
    
    lt = [root, root]
    
    while len(lt) > 0:
        lnode = lt.pop(0)
        rnode = lt.pop(0)        

        if lnode.val != rnode.val:
            return False
        else:
            if lnode.left != None and rnode.right != None:
                lt.append(lnode.left)
                lt.append(rnode.right)
            elif lnode.left != None or rnode.right != None:
                return False
            
            if lnode.right != None and rnode.left != None:
                lt.append(lnode.right)
                lt.append(rnode.left)
            elif lnode.right != None or rnode.left != None:
                return False
        
    return True




def tree_traversal(level, node):
    tmp_str = '|   ' * level + '+-'
    if node == None:
        print('%s <null>' %tmp_str)
    else:
        print('%s <%d>' %(tmp_str, node.val))
        tree_traversal(level + 1, node.left)
        tree_traversal(level + 1, node.right)
        
    

def tree_test():
    r = TreeNode(10)
    
    r.left = TreeNode(8)
    r.left.left = TreeNode(7)
    r.left.left.left = TreeNode(6)
    r.left.left.left.right = TreeNode(5)
     
    r.right = TreeNode(8)
    r.right.right = TreeNode(7)
    r.right.right.right = TreeNode(6)
    r.right.right.right.left = TreeNode(5)
    tree_traversal(0, r)
    return r
