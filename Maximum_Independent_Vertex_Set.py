
"""Maximum_Independent_Vertex_Set.py: Determine the (one) independent set of maximum cardinality vertices
        of a given non-oriented graph G, with n vertices and m edges, using an exhaustive search algorithm."""

__author__ = "Rafael Sá, 104552, rafael.sa@ua.pt, MEI"

import random


def print_graph(g):
    n = len(g)
    for i in range(n):
        print(" ", i, end="")
    print()
    for i in range(n):
        print(i, end=" ")
        for j in range(n):
            print(g[i][j], end="  ")
        print()
    print()


def generate_graph(v):
    """Generate and return graph with v vertices."""
    graph = [[0 for i in range(v)] for j in range(v)]
    for i in range(v):
        for j in range(v):
            if j != i:
                edge = random.randint(0, 1)
                graph[i][j] = edge;
                graph[j][i] = edge;
    return graph


def get_num_edges(g):
    """Return number of edges on graph g."""
    return sum(cell for row in g for cell in row)


if __name__ == '__main__':
    num_vertices = 3
    adjacency_matrix = generate_graph(num_vertices)
    print("Graph with " + str(num_vertices) + " vertices and " + str(get_num_edges(adjacency_matrix)) + " edges")
    print_graph(adjacency_matrix)
