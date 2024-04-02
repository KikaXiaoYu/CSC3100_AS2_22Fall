


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


class TreeArray:
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
    
    def calInterSum(self, l, r):
        return self.calSum(r)-self.calSum(l-1)

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

# the main
if (__name__ == "__main__"):
    num = int(input())
    tree_array = TreeArray()
    for i in range(num):
        g_oper_lst = [int(i) for i in input().split()]
        if g_oper_lst[0] == 1:
            tree_array.insert(g_oper_lst[1], g_oper_lst[2])
        if g_oper_lst[0] == 2:
            tree_array.delete(g_oper_lst[1])
        if g_oper_lst[0] == 3:
            print(tree_array.calInterSum(g_oper_lst[1], g_oper_lst[2]))
