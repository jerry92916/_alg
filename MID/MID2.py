import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # 用於 Kruskal 
        self.adj = [[] for _ in range(vertices)]  # 用於 Dijkstra 與 Prim 

    def add_edge(self, u, v, w):
        # u, v 為節點編號, w 為權重
        self.graph.append([u, v, w])
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    # Dijkstra 演算法 
    def dijkstra(self, src):
        distances = [float('inf')] * self.V
        distances[src] = 0
        pq = [(0, src)]  # (距離, 節點)

        while pq:
            d, u = heapq.heappop(pq)
            if d > distances[u]:
                continue
            for v, weight in self.adj[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    heapq.heappush(pq, (distances[v], v))
        return distances

    # Prim 演算法
    def prim(self):
        mst_weight = 0
        visited = [False] * self.V
        pq = [(0, 0)]  # (權重, 起點)
        edges_count = 0
        mst_edges = []

        while pq and edges_count < self.V:
            w, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            mst_weight += w
            if w != 0: edges_count += 1
            
            for v, weight in self.adj[u]:
                if not visited[v]:
                    heapq.heappush(pq, (weight, v))
        return mst_weight

    # Kruskal 演算法
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = list(range(self.V))
        rank = [0] * self.V

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            if root_u != root_v:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, root_u, root_v)
        
        return sum(edge[2] for edge in result)

# 測試與輸出
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print("=== 演算法運行結果 ===")
# Dijkstra
dists = g.dijkstra(0)
print(f"Dijkstra (從節點 0 開始的最短距離): {dists}")

# Prim
prim_res = g.prim()
print(f"Prim 演算法生成的 MST 總權重: {prim_res}")

# Kruskal
kruskal_res = g.kruskal()
print(f"Kruskal 演算法生成的 MST 總權重: {kruskal_res}")
