class ArrayNode:
  '''Node of Array-based Priority Queue
  
  Attributes:
      val (any): The actual value of the item
      priority (int): The priority level (The lower the number, the higher the priority)
  '''
  def __init__(self, val, priority):
    self.val = val
    self.priority = priority
  
  def __str__(self):
    return f"({self.val}, {self.priority})"

class ArrayPriorityQueue:
  def __init__(self):
    self.arr = []
  
  def enqueue(self, val, priority):
    self.arr.append(ArrayNode(val, priority))

  def peek_index(self):
    idx = -1
    max_priority = float('inf')
    
    for i, item in enumerate(self.arr):
      if item.priority < max_priority:
        idx = i
        max_priority = item.priority
    return idx

  def pop(self):
    idx = self.peek_index()
    item = self.arr[idx]
    if idx != -1:
      self.arr.pop(idx)
    return item

  def is_empty(self):
    return len(self.arr) == 0

if __name__ == "__main__":
  pq = ArrayPriorityQueue()
  pq.enqueue(6, 0)
  pq.enqueue(5, 2)
  pq.enqueue(3, 1)
  
  while not pq.is_empty():
    print(pq.pop())
  
  