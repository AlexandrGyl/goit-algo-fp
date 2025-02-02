import heapq
import networkx as nx
G = nx.Graph()

G.add_nodes_from(["R1", "R2", "R3", "R4", "R5", "S1", "S2", "S3", "S4", "S5", "C1", "C2", "C3", "C4"])

G.add_edges_from([
("R1", "R2", {"bandwidth": 1000, "weight": 1/1000}),
("R1", "S1", {"bandwidth": 200, "weight": 1/200}),
("R1", "S2", {"bandwidth": 150, "weight": 1/150}),
("R2", "R3", {"bandwidth": 800, "weight": 1/800}),
("R2", "S3", {"bandwidth": 300, "weight": 1/300}),
("R3", "R4", {"bandwidth": 1000, "weight": 1/1000}),
("R3", "S4", {"bandwidth": 250, "weight": 1/250}),
("R4", "R5", {"bandwidth": 2000, "weight": 1/2000}),
("R4", "S5", {"bandwidth": 400, "weight": 1/400}),
("R5", "C1", {"bandwidth": 100, "weight": 1/100}),
("R5", "C2", {"bandwidth": 100, "weight": 1/100}),
("S1", "C3", {"bandwidth": 50, "weight": 1/50}),
("S5", "C4", {"bandwidth": 70, "weight": 1/70}),
("S2", "S3", {"bandwidth": 100, "weight": 1/100}),
("S3", "S4", {"bandwidth": 150, "weight": 1/150}),
("R1", "C4", {"bandwidth": 70, "weight": 1/70}),
("R2", "C2", {"bandwidth": 100, "weight": 1/100})
])

def dijkstra_with_heap(G, source):
    # Ініціалізація відстаней до всіх вершин як безкінечність
    dist = {node: float('inf') for node in G.nodes()}
    dist[source] = 0
    
    # Піраміда (бінарна купа) для вибору вершини з мінімальною відстанню
    priority_queue = [(0, source)]  # (відстань, вершина)
    
    # Множина для відвіданих вершин
    visited = set()

    # Обробка кожної вершини
    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)  # Вибір вершини з мінімальною відстанню
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        # Перевірка всіх суміжних вершин
        for neighbor, attrs in G[current_node].items():
            weight = attrs['weight']
            distance = current_dist + weight
            
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return dist

# Використовуємо алгоритм Дейкстри для пошуку найкоротших шляхів від вершини 'R1'
shortest_paths = dijkstra_with_heap(G, 'R1')
print(shortest_paths)