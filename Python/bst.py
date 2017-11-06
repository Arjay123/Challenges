class BST(object):
    def __init__(self, value=None):
        if value:
            self.root = BSTNode(value, None)
        else:
            self.root = None

    def add(self, value):
        self.root = self.addhelper(value, None, self.root)

    def addhelper(self, value, parent, curr):
        if not curr:
            return BSTNode(value, parent)

        if value <= curr.value:
            curr.left = self.addhelper(value, curr, curr.left)
        else:
            curr.right = self.addhelper(value, curr, curr.right)

        return curr

    def find(self, value):
        return self.findhelper(value, self.root)

    def findhelper(self, value, node):
        if not node:
            return False

        if node.value == value:
            return True
        elif value < node.value:
            return self.findhelper(value, node.left)
        else:
            return self.findhelper(value, node.right)

    def delete(self, value):
        self.deletehelper(value, self.root)

    def deletehelper(self, value, node):
        if not node:
            return

        if node.value == value:
            if node.left and not node.right:
                node = node.left
            elif node.right and not node.left:
                node = node.right
            elif not node.right and not node.left:
                node = None
            else:
                min_right_tree = self.replacesmallest(node.right, value)
                node.value = min_right_tree
                node.right = self.deletehelper(value, node.right)
        elif value < node.value:
            node.left = self.deletehelper(value, node.left)
        else:
            node.right = self.deletehelper(value, node.right)

        return node


    def replacesmallest(self, node, value):
        if not node.left:
            old = node.value
            node.value = value
            return old
        return self.replacesmallest(node.left, value)


    def preorder(self):
        self.preorderhelper(self.root)

    def preorderhelper(self, node):
        if not node:
            return

        print node.value

        self.preorderhelper(node.left)
        self.preorderhelper(node.right)

    def postorder(self):
        self.postorderhelper(self.root)

    def postorderhelper(self, node):
        if not node:
            return

        self.postorderhelper(node.left)
        self.postorderhelper(node.right)
        print node.value

    def inorder(self):
        self.inorderhelper(self.root)

    def inorderhelper(self, node):
        if not node:
            return

        self.inorderhelper(node.left)
        print node.value
        self.inorderhelper(node.right)

    def levelorder(self):
        if self.root:
            self.levelorderhelper([self.root])

    def levelorderhelper(self, nodes):
        if len(nodes) == 0:
            return

        curr = nodes.pop(0)

        print curr.value
        if curr.left:
            nodes.append(curr.left)
        if curr.right:
            nodes.append(curr.right)
        self.levelorderhelper(nodes)


class BSTNode(object):
    def __init__(self, value, parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


t = BST()
t.add(5)
t.add(3)
t.add(2)
t.add(1)
t.add(4)
t.add(7)
t.add(6)
t.add(10)
t.add(11)
t.add(9)

print "Preorder"
print "--------"
t.preorder()
print ""
print "Postorder"
print "---------"
t.postorder()
print ""
print "Inorder"
print "-------"
t.inorder()
print ""
print "Levelorder"
print "----------"
t.levelorder()

print ""
t.delete(3)
t.delete(1)
t.delete(7)
t.preorder()
