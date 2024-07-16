class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.data = None



class Tree : 
    def createNode(self,data):
        # Create object of Node() tpye
        return Node(data)

    def insertNode(self,node,data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            self.insertNode(node.left,data)
        if data > node.data :
            self.insertNode(node.right,data)



        
