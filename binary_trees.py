class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 0
      # TODO complete Node initialization

  def __init__(self):
    self.__root = None
    self.__value_located = True
    self.__childs_height = 0


  def insert_element(self, value):
    self.__root = self.__recursive_insert(self.__root, value) 
    self.__childs_height = self.height_updater(self.__root)

      
    

  def __recursive_insert(self, node, new_value):
    if node is None: # base case that finds the empty node to place our new node
      node = Binary_Search_Tree.__BST_Node(new_value)
      self.height_updater(node)
      return node
    #elif node == new_value:
     # raise ValueError
    elif new_value < node.value: #sends nodes to left of parent
      node.left = self.__recursive_insert(node.left, new_value) #recursion that rebuilds the BST
      self.height_updater(node)
    elif new_value > node.value: #sends node to right of parent
      node.right = self.__recursive_insert(node.right, new_value) 
      self.height_updater(node)
    elif new_value == node.value:
      raise ValueError
    return node


  def remove_element(self, value):

    if self.__root is None:
      raise ValueError('Value not in tree.')
    if self.__root.left is None and self.__root.right is None and self.__root.value == value:
      self.__root = None
      self.__value_located = False
    #else:
    elif self.__root.left is not None or self.__root.right is not None:
      self.__root = self.__delete_node(self.__root, value)
    if self.__value_located is True:
      raise ValueError('Value not in tree.')
    self.__childs_height = self.height_updater(self.__root)

  
    
    
  def __delete_node(self, node, value):
    #if node.value != value:
     # return ValueError
    if node is None: 
      return None
    if node.value > value:
      node.left = self.__delete_node(node.left, value)
      self.height_updater(node)
    elif node.value < value:  
      node.right = self.__delete_node(node.right, value)
      self.height_updater(node)
    else:# node.value == value: #once it finds the node
      self.height_updater(node)
      self.__value_located = False
      if node.right is None: #if only one child on left
        replacement_node = node.left
        node = None
        return replacement_node
      elif node.left is None: #only one child on right
        replacement_node = node.right
        node = None
        return replacement_node
      #has two childs
      replacement_node = node.right
      while replacement_node.left is not None: #finds the smallest value 
        replacement_node = replacement_node.left
      node.value = replacement_node.value
      node.right = self.__delete_node(node.right, replacement_node.value)
    return node


  def height_updater(self, node):
    if node is None:
      return
    if node.left and node.right:
      node.height = max(node.left.height + 1, node.right.height + 1)
    elif node.right is None and node.left:
      node.height = node.left.height + 1
    elif node.left is None and node.right:
      node.height = node.right.height + 1
    else:
      node.height = 1
    #self.__childs_height = node.height
    return node.height


