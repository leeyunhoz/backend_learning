from collections import *
from subway_graph import *

def bfs(graph, start_node):
    queue = deque()
    
    for station_node in graph.values():
        station_node.visited = False
        station_node.predecessor = None
        
    start_node.visited = True
    queue.append(start_node)
    
    while queue:
        current_node = queue.popleft()
        
        for neighbor in current_node.adjacent_stations:
            if not neighbor.visited:
                neighbor.visited = True
                queue.append(neighbor)
                neighbor.predecessor = current_node
                

def back_track(destination_node):
    temp = destination_node
    res_str = ""
    while temp is not None:
        res_str = f"{temp.station_name} {res_str}"
        temp = temp.predecessor
        
    return res_str

stations = create_station_graph("./new_stations.txt")

bfs(stations, stations["을지로3가"])
print(back_track(stations["강동구청"]))
        
            
            