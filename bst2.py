class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create(nums):

    if not nums:
        return None
    mid_val = len(nums)//2
    node = TreeNode(nums[mid_val])
    node.left = create(nums[:mid_val])
    node.right = create(nums[mid_val+1:])
    return node

def insert(root, newValue):
    #if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root=TreeNode(newValue)
        return root
    #binary search tree is not empty, so we will insert it into the tree
    #if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue<root.val:
        root.left=insert(root.left,newValue)
    else:
        #if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.right=insert(root.right,newValue)
    return root

def preOrder(node):
    if not node:
        return
    print(node.val, height(node))
    preOrder(node.left)
    preOrder(node.right)

def search(root, number):
    if root == None:
        return None
    if number == root.val:
        return root.val
    if number < root.val:
        return search(root.left, number)
    if number > root.val:
        return search(root.right, number)
    return None

def height(root):
    #if root is None return 0
    if root==None:
        return 0
    #find height of left subtree
    hleft=height(root.left)
    #find the height of right subtree
    hright=height(root.right)
    #find max of hleft and hright, add 1 to it and return the value
    if hleft>hright:
        return hleft+1
    else:
        return hright+1

def checkBalancedBinaryTree(root):
    #if tree is empty,return True
    if root==None:
        return True
    #check height of left subtree
    lheight= height(root.left)
    rheight = height(root.right)
    #if difference in height is greater than 1, return False
    if(abs(lheight-rheight)>1):
        return False
    #check if left subtree is balanced
    lcheck=checkBalancedBinaryTree(root.left)
    #check if right subtree is balanced
    rcheck=checkBalancedBinaryTree(root.right)
    #if both subtree are balanced, return True
    if lcheck==True and rcheck==True:
        return True

tree = create([1, 2, 3, 4, 5, 6, 7])
bananced = checkBalancedBinaryTree(tree)
print(bananced)

tree = insert(tree,20)
bananced = checkBalancedBinaryTree(tree)
print(bananced)
preOrder(tree)

tree = insert(tree,10)
bananced = checkBalancedBinaryTree(tree)
print(bananced)

tree = insert(tree,17)
bananced = checkBalancedBinaryTree(tree)
print(bananced)

tree = insert(tree,18)
bananced = checkBalancedBinaryTree(tree)
print(bananced)

tree = insert(tree,19)
bananced = checkBalancedBinaryTree(tree)
print(bananced)

tree = insert(tree,21)
bananced = checkBalancedBinaryTree(tree)
print(bananced)

preOrder(tree)

result = search(tree,18)
print(result)
