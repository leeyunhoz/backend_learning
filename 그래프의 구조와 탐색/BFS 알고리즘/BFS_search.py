from collections import deque
from subway_graph import create_station_graph

def bfs(graph, start_node):
    queue = deque()
    
    for station in graph.values():
        station.visited = False
    
    queue.append(start_node)
    start_node.visited = True
    
    while queue:
        current_node = queue.popleft()
        
        for neighbor in current_node.adjacent_stations:
            if not neighbor.visited:
                neighbor.visited = True
                queue.append(neighbor)
                
stations = create_station_graph("./new_stations.txt")
gangnam_station = stations["강남"]
            

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
bfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들이 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들이 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)