class Node:
   def __init__(self, key):
      self.leftChild = None
      self.rightChild = None
      self.data = key

#if binary tree traversed in order we get a sorted keys in ascending order
# Create a function to perform inorder tree traversal
def InorderTraversal(root):
   if root:
      InorderTraversal(root.leftChild)
      print(root.data)
      InorderTraversal(root.rightChild)

# Create a function to perform postorder tree traversal
def PreorderTraversal(root):
   if root:
      print(root.data)
      PreorderTraversal(root.leftChild)
      PreorderTraversal(root.rightChild)

# Create a function to perform preorder tree traversal
def PostorderTraversal(root):
   if root:
      PostorderTraversal(root.leftChild)
      PostorderTraversal(root.rightChild)
      print(root.data)

# Main class
if __name__ == "__main__":
   root = Node(4)
   root.leftChild = Node(2)
   root.rightChild = Node(6)
   root.leftChild.leftChild = Node(1)
   root.leftChild.rightChild = Node(3)
   root.rightChild.leftChild = Node(5)
   root.rightChild.rightChild = Node(7)

   # Function call
   print("Inorder traversal of binary tree is")
   InorderTraversal(root)

   print("Preorder traversal of binary tree is")
   PreorderTraversal(root)

   print("Postorder traversal of binary tree is")
   PostorderTraversal(root)