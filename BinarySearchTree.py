class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

def print_inorder(node):
    print_inorder(node.left_child)
    print(node.data)
    print_inorder(node.right_child)
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def delete(self, data):
        node_to_delete = self.search(data)
        parent_node = node_to_delete.parent
        
        #node_to_delete가 leaf노드일 때
        if node_to_delete.right_child is None and node_to_delete.left_child is None:
            if node_to_delete is self.root:
                self.root = None
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = None
            elif node_to_delete is parent_node.right_child:
                parent_node.right_child = None
        
        #node_to_delete가 하나의 자식을 가질 때
        #node_to_delete가 왼쪽 자식을 가질  때
        elif node_to_delete.right_child is None:
            if node_to_delete is self.root:
                self.root = node_to_delete.left_child
            elif parent_node.left_child is node_to_delete:
                parent_node.left_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
            elif parent_node.right_child is node_to_delete:
                parent_node.right_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
        #node_to_delete가 오른쪽 자식을 가질 때
        elif node_to_delete.left_child is None:
            if node_to_delete is self.root:
                self.root = node_to_delete.right_child
            elif parent_node.left_child is node_to_delete:
                parent_node.left_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
            else:
                parent_node.right_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
        
        #node_to_delete가 두개의 자식을 가질 때
        
        successor = self.find_min(node_to_delete.right_child)
        node_to_delete.data = successor.data
        
        if successor.parent.left_child is successor:
            successor.parent.left_child = successor.right_child
        elif successor.parent.right_child is successor:
            successor.parent.right_child = successor.right_child
        
        if successor.right_child is not None:
            successor.right_child.parent = successor.parent
    @staticmethod
    def find_min(node):
        temp = node
        
        while True:
            if temp.left_child is None:
                break
            elif temp.left_child is not None:
                temp = temp.left_child
                
        return temp
            
    def search(self, data):
        current_node = self.root
        if current_node is None:
            return None
        
        while True:
            if current_node.data == data:
                return current_node
            elif current_node.data > data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
            
    def insert(self, data):
        new_node = Node(data)
        current_node = self.root
        if current_node is None:
            self.root = new_node
            return
        while True:
            if data > current_node.data:
                if current_node.right_child is None:
                    current_node.right_child = new_node
                    break
                else:
                    current_node = current_node.right_child
            elif data < current_node.data:
                if current_node.left_child is None:
                    current_node.left_child = new_node
                    break
                else:
                    current_node = current_node.left_child
                
    
        
    def print_sorted_tree(self):
        print_inorder(self.root)
        
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 자식이 두 개 다 있는 노드 삭제
bst.delete(7)
bst.delete(11)

bst.print_sorted_tree()
