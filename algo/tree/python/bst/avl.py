from __future__ import print_function


def height(root):
    if root is None:
        return 0
    return root.height


def single_rotate_right(w):
    """
             w 
           /   \
           x   C
         /  \
        A   B
       /  
      D
             x 
           /   \
          A    w
         /    /   \
        D    B     C
                
    """
    x = w.left
    w.left = x.right
    x.right = w
    x.height = max(height(x.right), height(x.left)) + 1
    w.height = max(height(w.right), height(w.left)) + 1
    return x


def single_rotate_left(w):
    """
         w 
        /  \
       C    x
          /  \
          A   B
              \
               D
          
            x
          /  \
         w    B 
        /  \   \
       C    A   D    
    """
    x = w.right
    w.right = x.left
    x.left = w
    x.height = max(height(x.right), height(x.left)) + 1
    w.height = max(height(w.right), height(w.left)) + 1
    return x


def double_rotate_left_right(w):
    """
             w 
           /   \
           x   C
         /  \
        A   B
             \  
             D
        
    Single left rotation on x 
             w 
           /   \
           B   C
         /  \
        x   D
       /  
      A
        
    Single right rotation on w
    """
    w.left = single_rotate_left(w.left)
    return single_rotate_right(w)


def double_rotate_right_left(w):
    """
          w 
        /   \
       C     x
            /
           B
          /  \ 
        A     C
        
    Single right rotation on x 
          w 
        /   \
       C     B
            /  \
           A    x
                /
                C
        
    Single left rotation on w
    """
    w.right = single_rotate_right(w.right)
    return single_rotate_left(w)


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 0


def avl_insert(root, data):
    if root is None:
        return Node(data)
    if data <= root.data:
        root.left = avl_insert(root.left, data)
        if (height(root.left) - height(root.right)) > 1:
            if data < root.data:
                root = single_rotate_right(root)
            else:
                root = double_rotate_left_right(root)
    else:
        root.right = avl_insert(root.right, data)
        if (height(root.right) - height(root.left)) > 1:
            if data > root.data:
                root = single_rotate_left(root)
            else:
                root = double_rotate_right_left(root)

    root.height = max(height(root.left), height(root.right)) + 1
    return root


def print_in_order(root):
    if root is None:
        return
    print_in_order(root.left)
    print('%d (h:%d), ' % (root.data, root.height), end='')
    print_in_order(root.right)

if __name__ =='__main__':
    root = None
    root = avl_insert(root, 7)
    root = avl_insert(root, 2)
    root = avl_insert(root, -6)
    root = avl_insert(root, 9)
    root = avl_insert(root, 8)
    root = avl_insert(root, 10)
    root = avl_insert(root, 13)
    root = avl_insert(root, 12)
    root = avl_insert(root, 11)

    print_in_order(root)
