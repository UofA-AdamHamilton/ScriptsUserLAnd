def tarjans_scc(graph):
    """
    Finds strongly connected components (SCCs) 
    in a directed graph using Tarjan's Algorithm.

    :param graph: dict representing adjacency
     list of the graph {node: [neighbors]}
    :return: List of strongly connected component
    s (each component is a list of nodes)
    """
    index = 0
    index_map = {}
    lowlink_map = {}
    stack = []
    on_stack = set()
    sccs = []

    def strongconnect(node):
        nonlocal index
        index_map[node] = index
        lowlink_map[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in index_map:
                # Neighbor has not been visited
                # yet
                strongconnect(neighbor)
                lowlink_map[node] = min(lowlink_map[node], lowlink_map[neighbor])
            elif neighbor in on_stack:
                # Neighbor is in stack, hence in
                # the current SCC
                lowlink_map[node] = min(lowlink_map[node], index_map[neighbor])
                # If node is a root node, pop th
                #e stack and generate an SCC
        if lowlink_map[node] == index_map[node]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == node:
                    break
            sccs.append(scc)
            
    for node in graph:         
        if node not in index_map:
            strongconnect(node)
    return sccs

if __name__ == "__main__":
    graph = {
            'A': ['B'],
            'B': ['C', 'E', 'F'],
            'C': ['D', 'G'],
            'D': ['C', 'H'],
            'E': ['A', 'F'],
            'F': ['G'],
            'G': ['F'],
            'H': ['D', 'G']
            }

    sccs = tarjans_scc(graph)
    print("Strongly Connected Components:")
    for scc in sccs:
        print(scc)                                                                                                                                                                                                                       
