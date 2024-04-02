
class Node: 
    def __init__(self, key ,value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        self.lnum = 0
        self.rnum = 0


class Tree:
    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def insert(self, key):
        if (self.root == None):
            self.root = Node(key)
            return 
        cur_node = self.root
        while (cur_node != None):
            last_node = cur_node
            if (key < cur_node.key):
                cur_node = cur_node.left
                direction = 1
            else:
                cur_node = cur_node.right
                direction = 2
        if (direction == 1):
            last_node.left = Node(key)
        else:
            last_node.right = Node(key)

    def getTree(self, node, res_lst):
        if (node.left != None):
            self.getTree(node.left, res_lst)
        res_lst.append(node.key)
        if (node.right != None):
            self.getTree(node.right, res_lst)
        return res_lst

if __name__ == "__main__":
    tree = Tree()
    tree.insert(0)
    tree.insert(1)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree.insert(8)
    tree.insert(9)
    tree.insert(6)
    res = tree.getTree(tree.root, [])
    print(res)