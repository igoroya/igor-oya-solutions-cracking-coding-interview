'''
Created on 29 Aug 2017

@author: igoroya
'''


class TreeNode(object):
    def __init__(self, name=None):
        '''
        A very simple node of a tree, all what is needed to work with trees in the exercises
        '''
        self.name = name
        self.children = []

    def __repr__(self):
        return "node: {} children {}".format(self.name.__repr__(), [child.name.__repr__() for child in self.children])



class BinaryTreeNode(object):
    def __init__(self, name=None):
        '''
        A very simple node of a tree, all what is needed to work with trees in the exercises
        '''
        self.name = name
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None:
            left = 'None'
        else:
            left = self.left.name.__repr__()
        if self.right is None:
            right = 'None'
        else:
            right = self.right.name.__repr__()


        return "node: {} l {}, r {}".format(self.name.__repr__(), left, right)