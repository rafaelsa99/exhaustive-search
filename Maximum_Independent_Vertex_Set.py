
"""Maximum_Independent_Vertex_Set.py: Determine the (one) independent set of maximum cardinality vertices
        of a given non-oriented graph G, with n vertices and m edges, using an exhaustive search algorithm."""

__author__ = "Rafael Sá, 104552, rafael.sa@ua.pt, MEI"

import random
from itertools import combinations


def print_graph(graph):
    n = len(graph)
    for i in range(n):
        print(" ", i, end="")
    print()
    for i in range(n):
        print(i, end=" ")
        for j in range(n):
            print(graph[i][j], end="  ")
        print()
    print()


def generate_graph(num_vert):
    """Generate and return graph with v vertices."""
    graph = [[0 for i in range(num_vert)] for j in range(num_vert)]
    for i in range(num_vert):
        for j in range(num_vert):
            if j != i:
                edge = random.randint(0, 1)
                graph[i][j] = edge
                graph[j][i] = edge
    return graph


def get_num_edges(graph):
    """Return number of edges on graph g."""
    return sum(cell for row in graph for cell in row) // 2


def check_independence(graph, subset):
    """Check if the subset of the G vertices is independent."""
    comb = combinations(subset, 2)
    for c in list(comb):
        if graph[c[0]][c[1]] == 1:
            return False
    return True


def get_all_maximum_independent_set(graph, num_vert):
    """Determine and return all maximum independent vertex sets of a graph g."""
    vertices = [i for i in range(num_vert)]
    best_candidate = []
    cardinality_best_candidate = 0
    for i in range(num_vert, 0, -1):
        comb = combinations(vertices, i)
        for c in list(comb):
            if check_independence(graph, c) and len(c) >= cardinality_best_candidate:
                best_candidate.append(c)
                cardinality_best_candidate = len(c)
            if len(c) < cardinality_best_candidate:
                return best_candidate
    return best_candidate


def get_maximum_independent_set(graph, num_vert):
    """Determine and return the first maximum independent vertex set of a graph g."""
    vertices = [i for i in range(num_vert)]
    for i in range(num_vert, 0, -1):
        comb = combinations(vertices, i)
        for c in list(comb):
            if check_independence(graph, c):
                return c
    return None


if __name__ == '__main__':
    num_vertices = 21
    adjacency_matrix = generate_graph(num_vertices)
    print("Graph with " + str(num_vertices) + " vertices and " + str(get_num_edges(adjacency_matrix)) + " edges")
    print_graph(adjacency_matrix)
    print("First Maximum Independent Vertex Set:")
    max_set = get_maximum_independent_set(adjacency_matrix, num_vertices)
    print(max_set)
    print("All Maximum Independent Vertex Sets:")
    list_sets = get_all_maximum_independent_set(adjacency_matrix, num_vertices)
    for subset in list(list_sets):
        print(subset)
