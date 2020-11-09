###TREES###
import sys
import threading

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def add_parent(self, parent):
        self.parent = parent
        parent.children.append(self)


    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p=p.parent
        return level

    def get_depth(self):
        if len(self.children) == 0:
            return 0
        return 1 + max(map(TreeNode.get_depth, self.children))
    def __str__(self):
        return self.data

def get_tree_depth(array):
    nodes = [None for x in range(len(array))]
    for i in range(len(array)):
        nodes[i] = (TreeNode(str(i)))

    #add parent strategy
    #for i in range(len(array)):
        #if array[i] != -1:
        #    nodes[i].add_parent(nodes[array[i]])

    #add child strategy
    for i in range(len(array)):
        if array[i] != -1:
            nodes[array[i]].add_child(nodes[i])

    root_index = array.index(-1)
    return (1 + nodes[root_index].get_depth())


def main():
    n = int(input())
    assert 1<= n <= 10**5
    input_list = list(map(int, input().split()))
    print(get_tree_depth(input_list))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
