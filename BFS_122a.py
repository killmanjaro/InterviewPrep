from collections import deque

def BFS(graph, start):
    distance = {} # use dict to store-> node : distance
    for node in graph: # for all verticies
        distance[node] = float('inf') # intialize distance to inf since we do not know distance
    distance[start] = 0 # first node set to distance 0

    queue = deque() # create queue, we use deque since poping is more efficient
    queue.append(start) # append first node to the queue

    while queue: # while the queue is not empty
        current_node = queue.popleft() # pop oldest element

        for neighbor in graph[current_node]: # for each neighbor of the current node
            if distance[neighbor] == float('inf'): # if the node has not beem accessed yet
                distance[neighbor] = distance[current_node] + 1 # set it to distance +1
                queue.append(neighbor) # append neighbor

    return distance # return distance dict


# implementation

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# start BFS from node 'A'
distances = BFS(graph, 'A')

# print results
print("Shortest distances from node 'A':")
for node, distance in distances.items():
    print(f"Node {node}: {distance}")