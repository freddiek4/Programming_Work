# A general tree implementation with sibling and child relationships

class Node:
    def __init__(self, data):
        self.data = data
        self.child = None
        self.sibling = None

    def insert_sibling(self, node):
        current_node = self
        while current_node.sibling:
            current_node = current_node.sibling
        current_node.sibling = node
        return node

    def insert_child(self, node):
        if not self.child:
            self.child = node
        else:
            self.child.insert_sibling(node)
        return node

    def is_equal(self, other):
        if not self and not other:
            return True
        if (not self and other) or (self and not other):
            return False
        if self.data != other.data:
            return False
        return self.child.is_equal(other.child) if self.child and other.child else True and \
               self.sibling.is_equal(other.sibling) if self.sibling and other.sibling else True

    def to_string(self):
        result = f"{self.data} :"
        child = self.child
        if child:
            result += " "
            while child:
                result += child.data
                child = child.sibling
                if child:
                    result += " "
        result += "\n"
        if self.child:
            result += f"# Child of {self.data}\n"
            result += self.child.to_string()
        if self.sibling:
            result += f"# Next sib of {self.data}\n"
            result += self.sibling.to_string()
        return result

class Tree:
    def __init__(self):
        self.root = Node("ROOT")

    def __del__(self):
        self.root = None

    def __eq__(self, other):
        return self.root.is_equal(other.root) if self.root and other.root else False

    def to_string(self):
        if not self.root:
            return ""
        result = f"# Tree rooted at {self.root.data}\n"
        result += "# The following lines are of the form:\n"
        result += "#   node: child1 child2...\n"
        result += self.root.to_string()
        result += "# End of Tree\n"
        return result

    def make_special_config_1(self, names):
        if len(names) < 20:
            return
        self.root = Node("ROOT")
        AABA = self.root.insert_sibling(Node(names[0]))
        ABAB = AABA.insert_sibling(Node(names[1]))
        ABBA = ABAB.insert_sibling(Node(names[2]))
        BABA = ABBA.insert_sibling(Node(names[3]))
        COBO = AABA.insert_child(Node(names[4]))
        COCO = COBO.insert_sibling(Node(names[5]))
        CODO = ABAB.insert_child(Node(names[6]))
        COFO = CODO.insert_sibling(Node(names[7]))
        COGO = ABBA.insert_child(Node(names[8]))
        COHO = COGO.insert_sibling(Node(names[9]))
        COJO = BABA.insert_child(Node(names[10]))
        COKO = COJO.insert_sibling(Node(names[11]))
        COBO.insert_child(Node(names[12]))
        COCO.insert_child(Node(names[13]))
        CODO.insert_child(Node(names[14]))
        COFO.insert_child(Node(names[15]))
        COGO.insert_child(Node(names[16]))
        COHO.insert_child(Node(names[17]))
        COJO.insert_child(Node(names[18]))
        COKO.insert_child(Node(names[19]))
