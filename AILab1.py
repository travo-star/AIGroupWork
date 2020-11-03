import networkx as nx
import matplotlib.pyplot as plt 

class Traverser:

    def __init__(self):
        self.end_search = False
        self.visited = []

    def greedy(self, graph, start, destination):
        queue = []
        queue.append(start)
        self.visited.append(start)
        print(f'Starting point -> {start}')

        while len(queue) > 0 and not self.end_search:
            min_stld = 99999
            min_child = {}

            current_node = queue.pop(0)

            for child in list(graph.adj[current_node]):
                if child is destination:
                    print(f'Destination -> {child}')
                    self.end_search = True
                    self.visited.append(child)
                    break
                else:
                  if hlsd_mapping[child] < min_stld:
                      min_stld = hlsd_mapping[child]
                      min_child = child
                      self.visited.append(child)
                            

            if(not self.end_search):                    
                queue.append(min_child)
                print(f'Next point -- {min_child}')
        return self.visited
                
 
    def ucs(self, G, start, destination):     
        queue = []
        queue.append(start)

        self.visited = []
        self.end_search = False
        
        self.visited.append(start)

        print(f'Starting point -> {start}')

        while len(queue) > 0 and not self.end_search:
            current_node = queue.pop(0)
            max_dist = 99999
            min_child = " "

            if current_node is destination:
                print(f'Destination -> {current_node}')
                self.end_search = True
                self.visited.append(current_node)
                break
            
            for child in list(G.adj[current_node]):
                    if current_node +  child and child + current_node not in self.visited:
                        w = G[current_node][child]["weight"]
                        if w < max_dist:
                            max_dist = w
                            min_child = child
                            self.visited.append(current_node + child)                               
            if(not self.end_search):      
                queue.append(min_child)
                print(f'Next Point -- {min_child}')
        return self.visited

G = nx.Graph()

E = [("Sports Complex", "Siwaka", {"weight": 450}), ("Siwaka", "Phase 1B", {"weight" : 230}), 
("Siwaka", "Phase 1A", {"weight" : 10}), ("Phase 1B", "Phase 2", {"weight": 112}),
("Phase 1A", "Phase 1B", {"weight": 100}), ("Phase 1B", "STC", {"weight" : 50}),  ("Phase 1A", "Phase 1B", {"weight" : 100}), ("Phase 1A", "Madaraka", {"weight": 850}),
("STC", "Parking Lot", {"weight": 250}), ("STC", "Phase 2", {"weight": 50}),
("Phase 2", "J1", {"weight": 600}), ("Phase 2", "Phase 3", {"weight": 500}),
("J1", "Madaraka", {"weight": 200}), ("Madaraka", "Parking Lot", {"weight": 700 }),
("Phase 3", "Parking Lot", {"weight": 350})]


N = ["Sports Complex", "Siwaka", "Phase 1A", "Phase 1B", "STC", "Phase 2", "Parking Lot", "Phase 3", "J1", "Madaraka"]

C = [(0, 10), (10, 10), (20, 10), (10, 5), (10, 2), (20, 5), (30, 0), (30, 3), (30, 5), (40, 5)]

hlsd = [730, 405, 380, 280, 213, 210, 0, 160, 500, 630]

P = { N[i] : v for i, v in enumerate(C) }
hlsd_mapping = { N[i] : v for i, v in enumerate(hlsd) }


G.add_nodes_from(N)
G.add_edges_from(E)

for k, l in P.items():
    G.nodes[k]['position'] = l

print(G["Sports Complex"]["Siwaka"]["weight"])

t1 = Traverser()
print('Greedy BFS:')
print(t1.greedy(G, "Sports Complex", "Parking Lot"))
print('\nEnd')


t2 = Traverser()
print('Uniform Cost Search (UCS):')
print(t2.ucs(G, "Sports Complex", "Parking Lot"))
print('\nEnd')


positions = nx.get_node_attributes(G, 'position')
labels = nx.get_edge_attributes(G, 'weight')


nx.draw_networkx(G, positions, node_size = 2000,)
nx.draw_networkx_edges(G, positions)
nx.draw_networkx_edge_labels(G, positions, edge_labels = labels)
plt.axis('off')
plt.show()