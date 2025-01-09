class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy


        return dfs(node) if node else None

def build_test_graph():
    # Tạo một đồ thị đơn giản để kiểm tra
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    return node1

def print_graph(node, visited=set()):
    if not node or node in visited:
        return
    visited.add(node)
    print(f"Node {node.val}: {[n.val for n in node.neighbors]}")
    for neighbor in node.neighbors:
        print_graph(neighbor, visited)

if __name__ == "__main__":
    # Tạo đồ thị mẫu
    test_graph = build_test_graph()

    # In đồ thị gốc
    print("Original graph:")
    print_graph(test_graph)

    # Clone đồ thị
    solution = Solution()
    cloned_graph = solution.cloneGraph(test_graph)

    # In đồ thị sao chép
    print("\nCloned graph:")
    print_graph(cloned_graph)
