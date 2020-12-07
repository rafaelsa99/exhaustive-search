
"""Maximum_Independent_Vertex_Set.py: Determine the (one) independent set of maximum cardinality vertices
        of a given non-oriented graph G, with n vertices and m edges, using an exhaustive search algorithm."""

__author__ = "Rafael Sá, 104552, rafael.sa@ua.pt, MEI"

import random
import time
import csv
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


def generate_graph(num_vert, percent_edges):
    """Generate and return graph with v vertices and the given percentage of edges."""
    graph = [[0 for i in range(num_vert)] for j in range(num_vert)]
    num_edges = 0
    while get_percentage_edges(num_edges, num_vert) < percent_edges:
        for i in range(num_vert):
            for j in range(num_vert):
                if j != i and graph[i][j] == 0:
                    edge = random.randint(0, 1)
                    graph[i][j] = edge
                    graph[j][i] = edge
                    num_edges += edge
                    if get_percentage_edges(num_edges, num_vert) >= percent_edges:
                        return graph
    return graph


def get_num_edges(graph):
    """Return number of edges on graph g."""
    return sum(cell for row in graph for cell in row) // 2


def get_percentage_edges(num_edges, num_vert):
    """Return percentage of edges."""
    max_edges = (num_vert * (num_vert - 1)) / 2
    if max_edges > 0:
        return int((num_edges / max_edges) * 100)
    return 0


def get_graph_percentage_edges(graph, num_vert):
    """Return percentage of edges on a graph."""
    max_edges = (num_vert * (num_vert - 1)) / 2
    num_edges = sum(cell for row in graph for cell in row) // 2
    if max_edges > 0:
        return int((num_edges / max_edges) * 100)
    return 0


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
        if i < cardinality_best_candidate:
            return best_candidate
        comb = combinations(vertices, i)
        for c in list(comb):
            if check_independence(graph, c) and len(c) >= cardinality_best_candidate:
                best_candidate.append(c)
                cardinality_best_candidate = len(c)
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
    filename_format_excel = "results_to_excel.csv"
    percentage_edges = [0, 25, 50, 75, 100]
    file_results = open(filename, "w")
    file_results_to_excel = open(filename_format_excel, "w", newline='')
    excel_writer = csv.writer(file_results_to_excel, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    min_vertices = 2
    max_vertices = 25
    file_results.write("Results for the problem: Maximum Independent Vertex Set\n")
    file_results.write("Testing between " + str(min_vertices) + " and " + str(max_vertices) + " vertices and for " +
                       str(percentage_edges) + "% of edges\n")
    excel_writer.writerow(['Percentage of Edges', 'Number of Vertices', 'Number of Verifications', 'Execution Time',
                           'Number of Maximum Independent Vertex Sets'])
    for pct_edges in list(percentage_edges):
        for num_vertices in range(min_vertices, max_vertices + 1, 1):
            file_results.write("\n--------------------------------------------------------------------------------\n\n")
            adjacency_matrix = generate_graph(num_vertices, pct_edges)
            file_results.write("Testing: " + str(num_vertices) + " vertices and " + str(pct_edges) + "% edges:\n\n")
            file_results.write("Graph with " + str(num_vertices) + " vertices and " +
                               str(get_num_edges(adjacency_matrix)) + " (" +
                               str(get_graph_percentage_edges(adjacency_matrix, num_vertices)) + "%) edges\n\n")
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
            file_results.write("Number of Maximum Independent Vertex Sets: " + str(len(list_sets)) + "\n")
            file_results.write("Number of candidate sets tested: " + str(count_verifications) + "\n")
            file_results.write(f"Execution time: {(end - start):.2f} seconds\n")
            excel_writer.writerow([pct_edges, num_vertices, count_verifications,
                                   (end - start), len(list_sets)])

    file_results.close()
    file_results_to_excel.close()
    print("\nResults written to the file: \"" + filename + "\"")
    print("Results to use in excel written to the file: \"" + filename_format_excel + "\"")
