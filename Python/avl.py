class AVLTree(object):
    """docstring for AVLTree"""
    def __init__(self):
        super(AVLTree, self).__init__()
        self.root = None


    def delete(self, val):
        self.root = self.delete_helper(self.root, val)

    def delete_helper(self, node, val):
        if not node:
            return

        if val < node.val:
            node.left = self.delete_helper(node.left, val)
        elif val > node.val:
            node.right = self.delete_helper(node.right, val)
        else:
            #one child or none
            if not (node.left and node.right):
                temp = None

                if not node.left:
                    temp = node.right
                else:
                    temp = node.left
                node = temp
            else:
                min_node = self.next_min(node.right)
                node.val = min_node.val
                node.right = self.delete_helper(node.right, node.val)

        if not node:
            return

        #balance
        balance = node.get_balance()

        if balance < -1:
            if node.left.get_balance() > 0:
                node.left = self.rotate_left(node.left)
            node = self.rotate_right(node)
        elif balance > 1:
            if node.right.get_balance() < 0:
                node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)

        return node

    def next_min(self, node):
        if node.left:
            return self.next_min(node.left)
        return node

    def insert(self, val):
        #create node
        self.root = self.insert_helper(self.root, val)

    def insert_helper(self, node, val):
        #bst insert
        if not node:
            return Node(val)

        if val <= node.val:
            node.left = self.insert_helper(node.left, val)
        else:
            node.right = self.insert_helper(node.right, val)

        balance = node.get_balance()

        if balance < -1:
            if node.left.get_balance() > 0:
                node.left = self.rotate_left(node.left)
            node = self.rotate_right(node)
        elif balance > 1:
            if node.right.get_balance() < 0:
                node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)

        return node


    def rotate_left(self, node):
        y = node.right
        node.right = y.left
        if y.left:
            y.left.parent = node

        y.parent = node.parent
        if not node.parent:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y
        return y


    def rotate_right(self, node):
        y = node.left
        node.left = y.right
        if y.right:
            y.right.parent = node

        y.parent = node.parent
        if not node.parent:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.right = node
        node.parent = y
        return y

    def print_tree(self):
        self.print_helper(self.root)

    def print_helper(self, node):
        if not node:
            return

        self.print_helper(node.left)
        print(node)
        self.print_helper(node.right)

#L heavy, L: 1, R: 0
#R heavy, L: 0, R: 1

# balance = R-L
#if -, Left heavy
#if +, right heavy

class Node(object):
    """docstring for Node"""
    def __init__(self, val=None):
        super(Node, self).__init__()

        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def get_balance(self):
        return Node._get_height(self.right) - Node._get_height(self.left)

    @property
    def height(self):
        return Node._get_height(self)

    @staticmethod
    def _get_height(node):
        if not node:
            return -1

        return 1+max(Node._get_height(node.left), Node._get_height(node.right))

    def __str__(self):
        left = None
        if self.left:
            left = self.left.val
        right = None
        if self.right:
            right = self.right.val
        return str(self.val) + ", left child: " + str(left) + ", right child: " + str(right)

tree = AVLTree()
tree.insert(5)
tree.insert(2)
tree.insert(9)
tree.insert(6)




tree.print_tree()
tree.delete(2)
print('')
tree.print_tree()

# x = Node('x')
# tree.root = x

# y = Node('y')
# A = Node('A')
# B = Node('B')
# C = Node('C')

# x.left = A
# A.parent = x

# x.right = C
# C.parent = x

# C.left = y
# y.parent = C

# y.right = B
# B.parent = y

# print("x left:%s " % x.left)
# print("x.right:%s" % x.right)
# print("y.left:%s" % y.left)
# print("y.right:%s" % y.right)
# print("c.left:%s" % C.left)

# print('')
# tree.rotate_left(y)

# print("x left:%s " % x.left)
# print("x.right:%s" % x.right)
# print("y.left:%s" % y.left)
# print("y.right:%s" % y.right)
# print("x.right.left:%s" % x.right.left)
# print("c.left:%s" % C.left)

# print('')
# tree.rotate_right(C)

# print("x left:%s " % x.left)
# print("x.right:%s" % x.right)
# print("B.left:%s" % B.left)
# print("B.right:%s" % B.right)
# print("x.right.left:%s" % x.right.left)
# print("c.left:%s" % C.left)



