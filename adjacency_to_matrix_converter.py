def adjacency_list_to_matrix(adjacency_list: dict):
  matrix = [[0 for _ in range(len(adjacency_list))] for _ in range(len(adjacency_list))]

  for vertex, neighbors in adjacency_list.items():
    for neighbor in neighbors:
      matrix[vertex][neighbor] = 1

  [print(row) for row in matrix]

  return matrix

adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})
adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]})
adjacency_list_to_matrix({0: [1], 1: [0]})
adjacency_list_to_matrix({0: [], 1: [], 2: []})