class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.color = 'red'




class RBTree:
    COLOR_RED = 'red'
    COLOR_BLACK = 'black'


    def __init__(self):
        self.root = None

    def add(self, new_data):
        new_node = None
        if self.root:
            new_node = self.bal_add(self.root, new_data)
            if not new_node:
                return False
        else:
            new_node = Node(new_data)
        self.root = new_node
        self.root.color = RBTree.COLOR_BLACK
        return True


    def bal_add(self, node, new_data):
        if node is None:
           return Node(new_data)
        if node.data > new_data:
            node.left = self.bal_add(node.left, new_data)
        elif node.data < new_data:
            node.right = self.bal_add(node.right, new_data)
        else:
            return None
        return self.balanced(node)

    def is_red (self, node):
        return node is not None and node.color == RBTree.COLOR_RED

    def swap_colors (self, node1, node2):
        node1.color, node2.color = node2.color, node1.color

    def rotate_left (self, my_node):
        child = my_node.right
        child_left = child.left
        child.left = my_node
        my_node.right = child_left
        return child

    def rotate_right (self, my_node):
        child = my_node.left
        child_right = child.right
        child.right = my_node
        my_node.left = child_right
        return child

    def balanced(self, node):
        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
            self.swap_colors(node, node.left)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
            self.swap_colors(node, node.right)
        if self.is_red(node.left) and self.is_red(node.right):
            node.color = RBTree.COLOR_RED
            node.left.color = RBTree.COLOR_BLACK
            node.right.color = RBTree.COLOR_BLACK
        return node

    def print_tree(self, node, space=0):
        if node is not None:
            self.print_tree(node.right, space + 10)
            print(" " * space + str(node.data) + f' ( {node.color} )')
            self.print_tree(node.left, space + 10)


if __name__ == "__main__":
    tree = RBTree()
    print('_____________________')
    print('Введите число, когда наиграетесь, введите пробел')
    while True:
        data = input()
        if data != " ":
            print('_____________________')
            tree.add(int(data))
            tree.print_tree(tree.root)
        else:
            break