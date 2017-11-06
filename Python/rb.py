class RedBlackTree:
    def __init__(self):
        self.root = None


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.color = "red"


    def black_height(self):
        return max(Node._black_height(self.left), Node._black_height(self.right))

    @staticmethod
    def _black_height(node):
        if not node:
            return 1

        if node.color == "black":
            return 1 + max(Node._black_height(node.left), Node._black_height(node.right))
        return max(Node._black_height(node.left), Node._black_height(node.right))


