'''
Tree Implementation in Python from preorder and inorder
level order traversal
preorder traversal

'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(inorder, st, ed, val):
    index = None
    # print("here")
    for i in range(st, ed+1):
        if inorder[i] == val:
            index = i
            break
    return index

def build_tree(preorder, inorder, st, ed):
    #base case
    if(st > ed):
        return None
    
    #recursive case
    val = preorder[0]
    preorder.pop(0)
    node = TreeNode(val)
    idx = search(inorder, st, ed, val)
    node.left = build_tree(preorder, inorder, st, idx-1)
    node.right = build_tree(preorder, inorder, idx+1, ed)
    return node


def preorder_traversal(root):
    if(root):
        print(root.val, end = " ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)
        
        
def bfs(root):
    q = list()
    q.append(root)
    while len(q):
        top = q[0]
        q.pop(0)
        print(top.val, end = " ")
        if(top.left):
            q.append(top.left)
        if top.right:
            q.append(top.right)
    print()


if __name__ == '__main__':
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder =  [4, 2, 5, 1, 6, 3, 7]
    root = build_tree(preorder, inorder, 0, len(inorder)-1)
    preorder_traversal(root)
    print()
    bfs(root)





