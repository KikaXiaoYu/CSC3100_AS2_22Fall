
from requests import delete


class Node: 
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        self.lele = 0
        self.rele = 0
        self.lsum = 0
        self.rsum = 0


class Tree:
    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def successor(self, node):
        if (node.right != None):
            return self.findMinNodeByRoot(node.right)
        res = node.parent
        cur_node = node
        while (res != None and cur_node == res.right):
            cur_node = res
            res = res.parent
        return res

    def predecessor(self, node):
        if (node.left != None):
            return self.findMaxNodeByRoot(node.left)
        res = node.parent
        cur_node = node
        while (res != None and cur_node == res.left):
            cur_node = res
            res = res.parent
        return res
        
    
    def insert(self, idx, value):
        # find node needed to add child
        curidx = idx
        new_node = Node(value)
        if (self.root == None):
            self.root = new_node
            return 
        cur_node = self.root
        while (cur_node != None):
            last_node = cur_node
            if (curidx <= cur_node.lele):
                cur_node.lele += 1
                cur_node.lsum += value
                cur_node = cur_node.left
                direction = 1
            else:
                curidx -= cur_node.lele + 1
                cur_node.rele += 1
                cur_node.rsum += value
                cur_node = cur_node.right
                direction = 2
        # add child by direction
        if (direction == 1):
            last_node.left = new_node
        else:
            last_node.right = new_node
        new_node.parent = last_node

    def deleteChildNone(self, cur_node, value):
        parent_node = cur_node.parent
            # for the first parent_node
        if (parent_node == None):
            self.root = None
        else:
            if (parent_node.left == cur_node):
                parent_node.left = None
                parent_node.lsum -= value
                parent_node.lele -= 1
            else:
                parent_node.right = None
                parent_node.rsum -= value
                parent_node.rele -= 1
        # for all parent_nodes
        while (parent_node.parent != None):
            cur_node = parent_node
            parent_node = cur_node.parent
            if (parent_node.left == cur_node):
                parent_node.lsum -= value
                parent_node.lele -= 1
            else:
                parent_node.rsum -= value
                parent_node.rele -= 1

    def deleteChildLeft(self, cur_node, value):
        parent_node = cur_node.parent
        next_node = cur_node.left
            # for the first parent_node
        if (parent_node == None):
            self.root = next_node
        else:
            next_node.parent = parent_node
            if (parent_node.left == cur_node):
                parent_node.left = next_node
                parent_node.lsum -= value
                parent_node.lele -= 1
            else:
                parent_node.right = next_node
                parent_node.rsum -= value
                parent_node.rele -= 1
        # for all parent_nodes
        while (parent_node.parent != None):
            cur_node = parent_node
            parent_node = cur_node.parent
            if (parent_node.left == cur_node):
                parent_node.lsum -= value
                parent_node.lele -= 1
            else:
                parent_node.rsum -= value
                parent_node.rele -= 1

    def deleteChildRight(self, cur_node, value):
        parent_node = cur_node.parent
        next_node = cur_node.right
            # for the first parent_node
        if (parent_node == None):
            self.root = next_node
        else:
            next_node.parent = parent_node
            if (parent_node.left == cur_node):
                parent_node.left = next_node
                parent_node.lsum -= value
                parent_node.lele -= 1
            else:
                parent_node.right = next_node
                parent_node.rsum -= value
                parent_node.rele -= 1
        # for all parent_nodes
        while (parent_node.parent != None):
            cur_node = parent_node
            parent_node = cur_node.parent
            if (parent_node.left == cur_node):
                parent_node.lsum -= value
                parent_node.lele -= 1
            else:
                parent_node.rsum -= value
                parent_node.rele -= 1

    def deleteChildBoth(self, cur_node, value):
        parent_node = cur_node.parent
        succ_node = self.successor(cur_node)
        print("succ_node.value", succ_node.value)
        new_value = succ_node.value
        del_value = new_value - cur_node.value
        cur_node.value = new_value
        while (parent_node != None):
            if (parent_node.left == cur_node):
                parent_node.lsum += del_value
            else:
                parent_node.rsum += del_value
            cur_node = parent_node
            parent_node = cur_node.parent

        value = succ_node.value
        if (succ_node.left == None and succ_node.right == None):
            self.deleteChildNone(succ_node, value)
        elif (succ_node.left != None and succ_node.right == None):
            self.deleteChildLeft(succ_node, value)
        elif (succ_node.left == None and succ_node.right != None):
            self.deleteChildRight(succ_node, value)
        else:
            self.deleteChildBoth(succ_node, value)

    def delete(self, k):
        # find node needed to delete
        idx = k - 1
        cur_node = self.findNodeByIdx(idx)
        value = cur_node.value
        if (cur_node.left == None and cur_node.right == None):
            self.deleteChildNone(cur_node, value)
        elif (cur_node.left != None and cur_node.right == None):
            self.deleteChildLeft(cur_node, value)
        elif (cur_node.left == None and cur_node.right != None):
            self.deleteChildRight(cur_node, value)
        else:
            self.deleteChildBoth(cur_node, value)
            

    def calSum(self, k):
        idx = k - 1
        res = 0
        if (idx == -1):
            return res
        cur_node = self.findNodeByIdx(idx)
        next_node = self.predecessor(self.findMinNodeByRoot(cur_node))
        res += cur_node.lsum + cur_node.value
        while (next_node != None):
            cur_node = next_node
            res += cur_node.lsum + cur_node.value
            next_node = self.predecessor(self.findMinNodeByRoot(cur_node))
        return res
    
    def findNodeByIdx(self, idx):
        curidx = idx
        cur_node = self.root
        while (curidx != cur_node.lele):
            if (curidx < cur_node.lele):
                cur_node = cur_node.left
            elif (curidx > cur_node.lele):
                curidx -= cur_node.lele + 1
                cur_node = cur_node.right
        return cur_node

    def findMinNodeByRoot(self, root):
        res = root
        while (res.left != None):
            res = res.left
        return res

    def findMaxNodeByRoot(self, root):
        res = root
        while (res.right != None):
            res = res.right
        return res

    def getTree(self, node, res_lst):
        if (node.left != None):
            self.getTree(node.left, res_lst)
        res_lst.append(node.value)
        if (node.right != None):
            self.getTree(node.right, res_lst)
        return res_lst
    
    def printTree(self, lst):
        if (len(lst)==0):
            return 
        new_lst = list()
        for cur_node in lst:
            if (cur_node == None):
                print("{0}".format("None"), end = "\t")
            else:
                if (cur_node.parent != None):
                    print("{0}:{1}".format(cur_node.parent.value, cur_node.value), end = "\t")
                else:
                    print("{0}:{1}".format("root:", cur_node.value), end = "\t")
                
            if (cur_node != None):
                new_lst.append(cur_node.left)
                new_lst.append(cur_node.right)
            # if (cur_node.right != None):
        print()
        self.printTree(new_lst)



if __name__ == "__main__":
    tree = Tree()
    tree.insert(0, 2)
    tree.insert(0, 5)
    tree.insert(1, 4)
    tree.insert(0, 1)
    tree.insert(0, 3)
    tree.insert(2, 3)
    tree.insert(2, 5)
    tree.insert(3, 8)
    tree.insert(6, 9)
    tree.insert(6, 6)
    tree.insert(10, 4)
    tree.insert(11, 3)
    tree.insert(10, 5)
    tree.insert(11, 8)
    print()
    print("tree.getTree(tree.root, [])")
    print(tree.getTree(tree.root, []))
    print()
    # tree.printTree([tree.root])
    # print()
    # print("tree.predecessor(tree.findNodeByIdx(i)).value")
    # print([tree.predecessor(tree.findNodeByIdx(i)).value for i in range(1, 14)])
    print()
    print("tree.calSum(i)")
    print([tree.calSum(i) for i in range(0, 15)])

    print("tree.delete(10)")
    # print("tree.delete(6)")
    # tree.delete(10)
    tree.delete(6)
    tree.printTree([tree.root])
    print("tree.getTree(tree.root, [])")
    print(tree.getTree(tree.root, []))
    print("tree.calSum(i)")
    print([tree.calSum(i) for i in range(0, 14)])
    # print(tree.findNodeByIdx(8).value)
    # print(tree.findNodeByIdx(8).lele)
    # print(tree.findNodeByIdx(8).rele)
    # print(tree.findNodeByIdx(8).lsum)
    # print(tree.findNodeByIdx(8).rsum)

