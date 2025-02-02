import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self.insert_recursive(self.root, new_node)
    
    def insert_recursive(self, current, new_node):
        if new_node.val < current.val:
            if current.left is None:
                current.left = new_node
            else:
                self.insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self.insert_recursive(current.right, new_node)

def generate_color(step, total_steps):
    # Генерація кольору на основі порядку відвідування вузла
    color_intensity = int(255 * (step / total_steps))  # від темного до світлого
    color = f"#{color_intensity:02X}{color_intensity:02X}F0"  # Генерація кольору в 16-річній системі RGB
    return color

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
    if node.left:
        graph.add_edge(node.id, node.left.id)
        l = x - 1 / 2 ** layer
        pos[node.left.id] = (l, y - 1)
        l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
        graph.add_edge(node.id, node.right.id)
        r = x + 1 / 2 ** layer
        pos[node.right.id] = (r, y - 1)
        r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs_stack(node, total_steps):
    stack = [node]
    visited_nodes = []
    step = 0
    while stack:
        current_node = stack.pop()
        if current_node:
            current_node.color = generate_color(step, total_steps)
            visited_nodes.append(current_node)
            step += 1
            # Додаємо правий вузол до стеку першим, щоб лівий обходився першим
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
    return visited_nodes

def bfs_queue(root, total_steps):
    queue = deque([root])
    visited_nodes = []
    step = 0
    while queue:
        node = queue.popleft()
        node.color = generate_color(step, total_steps)
        visited_nodes.append(node)
        step += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited_nodes

# Створення дерева через BST
input_values = input("Введіть вузли дерева через пробіл: ")
values = list(map(int, input_values.split()))


bst = BinarySearchTree()
for value in values:
    bst.insert(value)

# Обхід в глибину (DFS) без рекурсії
visited_nodes_dfs = dfs_stack(bst.root, 5)  # Всього 5 вузлів
draw_tree(bst.root)

# Обхід в ширину (BFS)
bfs_queue(bst.root, 5)  # Всього 5 вузлів
draw_tree(bst.root)