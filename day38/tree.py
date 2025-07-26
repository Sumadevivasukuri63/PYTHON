class Treenode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def preorder(root):
    if root==None:
        return
    print(root.val,end=" ")    #root    
    preorder(root.left)        #left
    preorder(root.right)       #right


def postorder(root):
    if root==None:
        return
    postorder(root.left)      #left
    postorder(root.right)     #right
    print(root.val,end=" ")   #root

def inorder(root):
    if root==None:
        return
    inorder(root.left)        #left
    print(root.val,end=" ")   #root
    postorder(root.right)     #right  

    
    
    

root=Treenode(1)
root.left=Treenode(2)
root.left.left=Treenode(4)
root.left.right=Treenode(5)
root.left.right.right=Treenode(11)
root.left.left.left=Treenode(9)
root.left.left.right=Treenode(10)
root.right=Treenode(3)
root.right.right=Treenode(6)
root.right.right.right=Treenode(8)
root.right.right.left=Treenode(7)

preorder(root)
print("\n")
postorder(root)
print("\n")
inorder(root)



        
        