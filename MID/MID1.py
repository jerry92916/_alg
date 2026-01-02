import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# 初始化資料與圖形
def setup_graph():
    adj = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H'],
        'E': ['H'],
        'F': ['H'],
        'G': [],
        'H': [] 
    }
    
    # 建立圖形物件
    G = nx.DiGraph(adj)
    
    # 讓 A 在最上面，H 在最下面
    pos = {
        'A': (0, 3), 
        'B': (-1.5, 2), 'C': (1.5, 2), 
        'D': (-2, 1), 'E': (-1, 1), 'F': (1, 1), 'G': (2, 1),
        'H': (0, 0)
    }
    return G, pos, adj

# BFS 演算法(廣度優先)
def run_bfs(start, adj):
    visited = []
    queue = deque([start])
    seen = {start}
    
    while queue:
        curr = queue.popleft() # 先進先出
        visited.append(curr)
        for nxt in adj.get(curr, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return visited

# DFS 演算法(深度優先)
def run_dfs(start, adj):
    visited = []
    seen = set()

    def dfs(node):
        seen.add(node)
        visited.append(node)
        # 一條路走到底
        for nxt in adj.get(node, []):
            if nxt not in seen:
                dfs(nxt)
    
    dfs(start)
    return visited

# 執行與繪圖比較
def main():
    G, pos, adj = setup_graph()
    
    bfs_path = run_bfs('A', adj)
    dfs_path = run_dfs('A', adj)

    plt.figure(figsize=(14, 6))

    def draw_path(path, title, idx, color):
        plt.subplot(1, 2, idx)
        plt.title(title, fontsize=15)
        
        nx.draw(G, pos, with_labels=True, node_color='lightgray', 
                node_size=800, edge_color='#D1D1D1', arrowsize=20)
        
        step_labels = {node: f"\n\nStep {i+1}" for i, node in enumerate(path)}
        nx.draw_networkx_labels(G, pos, labels=step_labels, font_color='red', font_weight='bold')
        
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color=color, node_size=800)

    # 繪製 BFS 比較圖
    draw_path(bfs_path, "BFS (Horizontal Search)\nLevel by Level", 1, 'skyblue')
    
    # 繪製 DFS 比較圖
    draw_path(dfs_path, "DFS (Vertical Search)\nGo Deep First", 2, 'lightgreen')

    plt.tight_layout()
    print(f"BFS 順序: {bfs_path}")
    print(f"DFS 順序: {dfs_path}")
    plt.show()

if __name__ == "__main__":
    main()
