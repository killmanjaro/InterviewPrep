def DFS_visit(u, graph, color, d, f, time):
    '''
    u is the current vertex
    graph is the graph we are preforming on
    color is a dictionary of the colors in the graph
    d is a dictionary of the discovery time of vertices in the graph
    f is a dictionary of the finish time of vertices in the graph
    time is a variable we use to keep track of the discovery and start time of vertices
    '''
    color[u] = "gray"
    time += 1
    d[u] = time # discovery time

    for v in graph[u]: # for all verticies adjacent to u
        if color[v] == 'white': # if they are not visited yet
            DFS_visit(v, graph, color, d, f, time)

    color[u] = 'black' # node is finished
    time += 1
    f[u] = time # add time to finish time dict



def DFS(graph):
    color = {} # dict of colors (dict serving as graph in python)
    d = {} # discovery time
    f = {} # finish time
    time = 0

    # intialize all verticies as white, with no discovery/finish time
    for u in graph: 
        color[u] = 'white' 
        d[u] = 0 
        f[u] = 0

    for u in graph:
        if color[u] == 'white': # if the vertex has not been visited yet
            DFS_visit(u, graph, color, d, f, time)

    return d, f

    
if __name__ == "__main__":
    # Example graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': ['D'],
    }

    discovery_times, finish_times = DFS(graph)
    print("Discovery times:", discovery_times)
    print("Finish times:", finish_times)