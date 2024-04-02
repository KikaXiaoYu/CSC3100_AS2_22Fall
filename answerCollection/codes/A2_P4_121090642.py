
class Node: 
    def __init__(self, value, left = None, right = None):
        self.value = value # value of the Node
        self.left = left # left child Node
        self.right = right # right child Node
        self.parent = None # parent Node
        self.lele = 0 # total num of element at left
        self.rele = 0 # total num of element at right
        self.lsum = 0 # total sum of value of element at left
        self.rsum = 0 # total sum of value of element at right

class TreeArray:
    def __init__(self, root = None):
        self.root = root # root 

    # get the next node of the para node in array order 
    def successor(self, node):
        if (node.right != None):
            return self.findMinNodeByRoot(node.right)
        res = node.parent
        cur_node = node
        while (res != None and cur_node == res.right):
            cur_node = res
            res = res.parent
        return res

    # get the previous node of the para node in array order 
    def predecessor(self, node):
        if (node.left != None):
            return self.findMaxNodeByRoot(node.left)
        res = node.parent
        cur_node = node
        while (res != None and cur_node == res.left):
            cur_node = res
            res = res.parent
        return res
        
    # insert a node with value after idx
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
            # idx <= cur, should be placed left 
            if (curidx <= cur_node.lele):
                cur_node.lele += 1
                cur_node.lsum += value
                cur_node = cur_node.left
                direction = 1 # left
            else:  # idx > cur, should be placed right
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

    # delete node with no child
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
        # for all next parent_nodes
        while (parent_node.parent != None):
            cur_node = parent_node
            parent_node = cur_node.parent
            if (parent_node.left == cur_node):
                parent_node.lsum -= value
                parent_node.lele -= 1
            else:
                parent_node.rsum -= value
                parent_node.rele -= 1

    # delete node with only left node
    def deleteChildLeft(self, cur_node, value):
        parent_node = cur_node.parent
        next_node = cur_node.left
        # for the first parent_node
        if (parent_node == None):
            self.root = next_node
            next_node.parent = None
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
        # for all next parent_nodes
        while (parent_node.parent != None):
            cur_node = parent_node
            parent_node = cur_node.parent
            if (parent_node.left == cur_node):
                parent_node.lsum -= value
                parent_node.lele -= 1
            else:
                parent_node.rsum -= value
                parent_node.rele -= 1

    # delete node with only right node
    def deleteChildRight(self, cur_node, value):
        parent_node = cur_node.parent
        next_node = cur_node.right
        # for the first parent_node
        if (parent_node == None):
            self.root = next_node
            next_node.parent = None
            return 
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
        # for all next parent_nodes
        while (parent_node.parent != None):
            cur_node = parent_node
            parent_node = cur_node.parent
            if (parent_node.left == cur_node):
                parent_node.lsum -= value
                parent_node.lele -= 1
            else:
                parent_node.rsum -= value
                parent_node.rele -= 1

    # delete node with both left and right node
    def deleteChildBoth(self, cur_node, value):
        # for the cur_node
        parent_node = cur_node.parent
        succ_node = self.successor(cur_node)
        new_value = succ_node.value
        del_value = new_value - value
        cur_node.value = new_value
        while (parent_node != None):
            if (parent_node.left == cur_node):
                parent_node.lsum += del_value
            else:
                parent_node.rsum += del_value
            cur_node = parent_node
            parent_node = cur_node.parent
        # for the node replacing the cur_node
        self.deleteByNode(succ_node)

    # delete node using node para
    def deleteByNode(self, node):
        value = node.value
        if (node.left == None and node.right == None):
            self.deleteChildNone(node, value)
        elif (node.left != None and node.right == None):
            self.deleteChildLeft(node, value)
        elif (node.left == None and node.right != None):
            self.deleteChildRight(node, value)
        else:
            self.deleteChildBoth(node, value)

    # delete node using idx para
    def deleteByIdx(self, k):
        # find node needed to delete
        idx = k - 1
        cur_node = self.findNodeByIdx(idx)
        self.deleteByNode(cur_node)
            
    # calculate the sum from 1st to kth
    # if k = 0, then return 0
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
    
    # calculate the sum from lth to rth
    def calInterSum(self, l, r):
        return self.calSum(r)-self.calSum(l-1)

    # find a node by its idx
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

    # find the minimun node from node
    def findMinNodeByRoot(self, root):
        res = root
        while (res.left != None):
            res = res.left
        return res

    # find the maximun node from node
    def findMaxNodeByRoot(self, root):
        res = root
        while (res.right != None):
            res = res.right
        return res

# the main
if (__name__ == "__main__"):
    num = int(input())
    tree_array = TreeArray()
    for i in range(num):
        g_oper_lst = [int(i) for i in input().split()]
        if g_oper_lst[0] == 1:
            tree_array.insert(g_oper_lst[1], g_oper_lst[2])
        if g_oper_lst[0] == 2:
            tree_array.deleteByIdx(g_oper_lst[1])
        if g_oper_lst[0] == 3:
            print(tree_array.calInterSum(g_oper_lst[1], g_oper_lst[2]))
