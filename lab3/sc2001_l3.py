
def infinite_knapsack(N, C, w, p):
  profit = [[0 for j in range(C + 1)] for i in range(N + 1)]
  for item in range(1, N + 1):
    for cap in range(1, C + 1):
      if cap < w[item]:
        profit[item][cap] = profit[item - 1][cap]
      else:
        profit[item][cap] = max(profit[item - 1][cap], 
                p[item] + profit[item][cap - w[item]],
                p[item] + profit[item - 1][cap - w[item]])
  return profit

def find_item(N, C, w, profit):
  item, cap = N, C
  path = []
  while item > 0 and cap > 0:
    if profit[item][cap] == profit[item - 1][cap]:
      item = item - 1
    else:
      cap = cap - w[item]
      if cap < 0: break
      path.append(item)
  return path

def print_2d(arr):
  for row in arr:
    for num in row:
      print(f"{num:<3}", end=" ")
    print()

if __name__ == "__main__":
  N = 3
  C = 14
  w = [0, 4, 6, 8]
  p = [0, 7, 6, 9]
  
  profit = infinite_knapsack(N, C, w, p)
  path = find_item(N, C, w, profit)
  
  print("Knapsack Array:"); print_2d(profit)
  print(f"Maximum Profit = {profit[N][C]}")
  print(f"Taken Item History = {path}")
  
      
    
          
      