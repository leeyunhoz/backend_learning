from collections import *
from subway_graph import *

def dfs(graph, start_node):
    stack = deque()
    for station_node in graph.values():
        station_node.visited = 0
    
    start_node.visited = 1
    stack.append(start_node)
    
    while stack:
        current_node = stack.pop()
        current_node.visited = 2
        
        for neighbor in current_node.adjacent_stations:
            if neighbor.visited == 0:
                neighbor.visited = 1
                stack.append(neighbor)
    
stations = create_station_graph("./new_stations.txt")

gangnam_station = stations["강남"]

dfs(stations, gangnam_station)

print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)

