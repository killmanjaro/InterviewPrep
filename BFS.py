from collections import deque
'''
bfs algorithm 
Uses a graph, starts with source node and then traverses all its adjacent sides
once all adjacents have been traversed, we move on to next set

uses a queue, we first push first node into queue, then visit unvisited neighbors and push into queue
'''

# s is source node
def bfs(adj, s):
    q = deque()

    # mark all verticies as not visited
    visited = [False] * len(adj)
    # visited is a list, containing false 

    visited[s] = True
    q.append(s) # add s to the queue
    print("Adding", s,"to the queue")

    while q: # while there are elements in the queue
        curr = q.popleft() # dequeue a vertex and print it
        print("Dequeued vertex", curr)

        for x in adj[curr]: # get all adj verticies of the vertex we just dequeued
            if not visited[x]: # if the verticie is not visited
                visited[x] = True # mark it as visited
                q.append(x) # add it to the queue
                print("Adding adjacent vertex", x)

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
  
    # Number of vertices in the graph
    V = 5

    # Adjacency list representation of the graph
    adj = [[] for _ in range(V)]

    # Add edges to the graph
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)

    # Perform BFS traversal starting from vertex 0
    print("BFS starting from 0: ")
    bfs(adj, 0)