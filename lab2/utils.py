import numpy as np
import random

def adj_matrix_converter(adj_list, n):
    adj_matrix = np.zeros(shape=(n, n))
    for idx, vertex in enumerate(adj_list.keys()):
        for dest, weight in adj_list[vertex]:
            adj_matrix[idx][dest] = weight
    return adj_matrix 
  
def printPath(path):
    if not path:
        print("Start Node")
        return    
    for node in path:
        print(node, end = "->")
    print()

def print_adj_list(adj_list):
  print("Format: Neighbor[Weight]\n", end="")
  for vertex in adj_list:
    print(f"{vertex}: ", end="")
    for neighbor, weight in adj_list[vertex]:
      print(f"{neighbor}[ {weight} ], ", end="")
    print()
    
def count_edges(adj_list):
  total_count = 0
  for vertex in adj_list:
    total_count += len(adj_list[vertex])
  return total_count

def general_graph_generator(node_size, prob=0.5, max_weight=10):
  adj_list = {i:[] for i in range(node_size)}
  vertices = [i for i in range(node_size)]

  for node in vertices:
    success_count = 0 #to ensure no node that has degree 0
    while(success_count <= 0):
      for neighbor in vertices:
        if neighbor == node: continue
        if random.random() - prob < 1e-5:
          weight = random.randint(1, max_weight)
          adj_list[node].append((neighbor, weight))
          success_count += 1
  return adj_list

def undirected_graph_generator(node_size, prob=0.5, max_weight=10):
  adj_list = {i:[] for i in range(node_size)}
  vertices = [i for i in range(node_size)]
  
  for i, node in enumerate(vertices):
    success_count = 0 #to ensure no node that has degree 0
    while(success_count <= 0):
      success_count = len(adj_list[node])
      for j, neighbor in enumerate(vertices):
        if neighbor == node or j < i: continue
        
        if random.random() - prob < 1e-5:
          weight = random.randint(1, max_weight)
          adj_list[node].append((neighbor, weight))
          adj_list[neighbor].append((node, weight))
          success_count += 1
  return adj_list

def connected_graph_generator(node_size, max_weight=10):
  return general_graph_generator(node_size, 1.0, max_weight)

def connected_undirected_graph_generator(node_size, max_weight=10):
  return undirected_graph_generator(node_size, 1.0, max_weight)

if __name__ == "__main__":
  #print_adj_list(connected_undirected_graph_generator(100))
  adj_list = general_graph_generator(100)
  print_adj_list(adj_list)
  print(count_edges(adj_list))
  
  
  
  