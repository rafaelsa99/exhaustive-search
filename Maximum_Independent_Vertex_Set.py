
"""Maximum_Independent_Vertex_Set.py: Determine the (one) independent set of maximum cardinality vertices
        of a given non-oriented graph G, with n vertices and m edges, using an exhaustive search algorithm."""

__author__ = "Rafael Sá, 104552, rafael.sa@ua.pt, MEI"

import random
import time
from itertools import combinations

count_verifications = 0


def print_graph(graph, file):
    n = len(graph)
    for i in range(n):
        file.write("\t" + str(i))
    file.write("\n")
    for i in range(n):
        file.write(str(i) + "\t")
        for j in range(n):
            file.write(str(graph[i][j]) + "\t")
        file.write("\n")
    file.write("\n")


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


def check_independence(graph, candidate_subset):
    """Check if the candidate subset of the G vertices is independent."""
    global count_verifications
    count_verifications += 1
    comb = combinations(candidate_subset, 2)
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
    filename = "results.txt"
    file_results = open(filename, "w")
    num_vertices = 15
    adjacency_matrix = generate_graph(num_vertices)
    file_results.write("Graph with " + str(num_vertices) + " vertices and " +
                       str(get_num_edges(adjacency_matrix)) + " edges\n\n")
    print_graph(adjacency_matrix, file_results)

    file_results.write("First Maximum Independent Vertex Set:\n")
    start = time.time()
    max_set = get_maximum_independent_set(adjacency_matrix, num_vertices)
    end = time.time()
    file_results.write("\t" + str(max_set) + "\n")
    file_results.write("Number of candidate sets tested: " + str(count_verifications) + "\n")
    file_results.write(f"Execution time: {(end - start):.2f} seconds\n")

    file_results.write("\n")
    count_verifications = 0
    file_results.write("All Maximum Independent Vertex Sets:\n")
    start = time.time()
    list_sets = get_all_maximum_independent_set(adjacency_matrix, num_vertices)
    end = time.time()
    for subset in list(list_sets):
        file_results.write("\t" + str(subset) + "\n")
    file_results.write("Number of candidate sets tested: " + str(count_verifications) + "\n")
    file_results.write(f"Execution time: {(end - start):.2f} seconds\n")

    print("\nResults written to the file: \"" + filename + "\"")
