class StationNode:
    def __init__(self, station_name):
        self.station_name = station_name
        self.visited = 0
        self.adjacent_stations = []
        
    def add_connection(self, other_station):
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)
        
def create_station_graph(input_file):
    stations = {}
    
    with open(input_file) as raw_station_file:
        for line in raw_station_file:
            previous_station = None
            subway_line = line.strip().split("-")
            
            for name in subway_line:
                station_name = name.strip()
                
                if station_name not in stations:
                    current_station = StationNode(station_name)
                    stations[station_name] = current_station
                else:
                    current_station = stations[station_name]
                
                if previous_station is not None:
                    current_station.add_connection(previous_station)
                
                previous_station = current_station
    
    return stations
                    