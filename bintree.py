class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = self.right = None
 
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            self.insert_help(self.root, key)
        return

    def insert_help(self, rt, key):
        if rt == None:
            rt = Node(key)
            return
        if rt.key > key:
            if rt.left:
                self.insert_help(rt.left, key)
            else:
                rt.left = Node(key)
        else:
            if rt.right:
                self.insert_help(rt.right, key)
            else:
                rt.right = Node(key)
        return rt


    def search(self, key):
        return self.search_help(self.root, key)

    def search_help(self, rt, key):
        if not rt:
            return False
        elif rt.key > key:
            return self.search_help(rt.left, key)
        elif rt.key < key:
            return self.search_help(rt.right, key)
        return True

    def remove(self, key):
        return self.remove_help(self.root, key)

    def remove_help(self, rt, key):
        if not rt:
            return
        if rt.key > key:
            if rt.left:
                rt.left = self.remove_help(rt.left, key)
        elif rt.key < key:
            if rt.right:
                rt.right = self.remove_help(rt.right, key)
        else:
            if rt.left == None:
                return rt.right
            elif rt.right == None:
                return rt.left
            else:
                temp = self.getmax(rt.left)
                rt.key = temp.key
                rt.left = self.deletemax(rt.left)
        return rt

    def getmax(self, rt):
        if rt.right == None:
            return rt
        return self.getmax(rt.right)

    def deletemax(self, rt):
        if rt.right == None:
            return rt.left
        rt.right = self.deletemax(rt.right)
        return rt
        
    def breadthfirst(self):
        self.breadthfirst_help(self.root)
        print()
        return

    def breadthfirst_help(self, rt):
        if not rt:
            return
        queue = []
        queue.append(rt)
        while(len(queue) != 0):
            current = queue[0]
            print(current.key, end=" ")
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
            queue.pop(0)

    def preorder(self):
        self.preorder_help(self.root)
        print()
        return
    
    def preorder_help(self, rt):
        if not rt:
            return
        print(rt.key,end=" ")
        self.preorder_help(rt.left)
        self.preorder_help(rt.right)
        return


if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 4, 6, 2]
    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6
    Tree.breadthfirst()     # 5 1 9 3 7 2 4 6