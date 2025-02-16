from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left:
                self._insert_recursive(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert_recursive(node.right, val)
            else:
                node.right = TreeNode(val)

    def search(self, val):
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        if val < node.val:
            return self._search_recursive(node.left, val)
        return self._search_recursive(node.right, val)
    
    
    def dfs(self, data):
        return self._dfs_recursive(self.root, data)

    def _dfs_recursive(self, node, data):
        if node:
            print(node.val)
        if node is None:
            return False
        if node.val == data:
            return True
        if self._dfs_recursive(node.left, data):
            return True
        if self._dfs_recursive(node.right, data):
            return True
        
    def bfs(self, data):
        if self.root is None:
            return False
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            print(node.val)
            if node.val == data:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.val)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.val)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.val)
            self._inorder_traversal(node.right, result)


tree = BinaryTree()
values_to_insert = [10, 5, 15, 3, 7, 12, 18]
for val in values_to_insert:
    tree.insert(val)

print(tree.search(7))
print(tree.search(14))
print(tree.search(10))
print(tree.search(18))

print("Preorder Traversal:", tree.preorder_traversal())
print("Inorder Traversal:", tree.inorder_traversal())
print("Postorder Traversal:", tree.postorder_traversal())
print("DFS:", tree.dfs(1))
print("BFS:", tree.bfs(1))
