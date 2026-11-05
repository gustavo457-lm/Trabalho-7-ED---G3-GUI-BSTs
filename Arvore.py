class Node:
    def __init__(self, item):
        self.item=item
        self.right=None
        self.left=None

class BST:
    def __init__(self):
        self.root = None

    def put(self, x, item):

        if x is None:
            return Node(item)
        
        elif item>x.item:
            x.right=self.put(x.right, item)
        elif item<x.item:
            x.left=self.put(x.left, item)

        return x

    def size(self, x):
        if x is None:
            return 0
        else:
           return 1 + self.size(x.left)+self.size(x.right)
        
       

    def height(self, x):
        if x is None:
            return -1
        else:
            return 1+max(self.height(x.left), self.height(x.right))

        
    def preOrder(self, node):
        if node is None:
            return node
        print(node.item)
        self.preOrder(node.left)
        self.preOrder(node.right)

    


tree=BST()

tree.root=Node(4)
tree.put(tree.root, 3)
tree.put(tree.root, 10)
tree.put(tree.root, 7)
tree.put(tree.root, 9)
tree.put(tree.root, 2)
tree.put(tree.root, 0)
tree.put(tree.root, 9)
tree.preOrder(tree.root)
print("----")

print(tree.height(tree.root))
print('----')
print(tree.size(tree.root))

     
        
            
        

    
       
           


        


    





        
       

        