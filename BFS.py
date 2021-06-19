# -*- coding: utf-8 -*-
"""
BFS:

    1) Pick a random node --> visit adjcement 
    2) 
    3)
    4)
"""
from queue import Queue

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited_dic = {} # dictionary flase/true for not-visited/visited
for key in graph.keys():
    visited_dic[key] = False

queue = Queue()    #Initialize a queue

prev_node_dic = {}
for key in graph.keys():
    prev_node_dic[key] = None

def bfs(graph, s_node, t_node):
    prev_node_dic = solve_path(graph, s_node, t_node)
    final_path = reconstruct(prev_node_dic, s_node, t_node)
    
    return final_path


def solve_path(graph, s_node, t_node):
    queue.put(s_node)
    visited_dic[s_node] = True
    
    while not queue.empty():
        current_node = queue.get()
        neighbors = graph[current_node]
        for neighbor in neighbors:
            if visited_dic[neighbor] == False:
                queue.put(neighbor)
                visited_dic[neighbor] = True
                prev_node_dic[neighbor] = current_node
    
    return prev_node_dic
    
    
def reconstruct(prev_node_dic, s_node, t_node):
    reverse_path = []
    current_node = t_node
    while True:
        reverse_path.append(current_node)
        #print(current_node)
        if prev_node_dic[current_node] != None and current_node != s_node:
            current_node = prev_node_dic[current_node]
        else:
            break
    
    if reverse_path[-1] == s_node:
        reverse_path.reverse()
        return reverse_path
    else:
        return []

if __name__ == "__main__":
    path = bfs(graph, s_node = 'A', t_node = 'F')
    print(path)