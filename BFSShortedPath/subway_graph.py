class StationNode:
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []
        self.visited = False
    
    def add_connection(self, other_station):
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)
        
def create_station_graph(input_file):
    stations = {}
    
    with open(input_file) as stations_raw_file:
        for line in stations_raw_file:
            previous_node = None
            subway_line = line.strip().split("-")
            
            for name in subway_line:
                station_name = name.strip()
                
                if station_name not in stations:
                    current_node = StationNode(station_name)
                    stations[station_name] = current_node
                else:
                    current_node = stations[station_name]
                
                if previous_node is not None:
                    current_node.add_connection(previous_node)
                
                previous_node = current_node
                
    return stations 