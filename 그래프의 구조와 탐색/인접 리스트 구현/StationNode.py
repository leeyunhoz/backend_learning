class StationNode:
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []
        
    def add_connection(self, other_station):
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)
        
    def __str__(self):
        res_str = f"{self.station_name}: "
        
        for station in self.adjacent_stations:
            res_str += f"{station.station_name} "
            
        return res_str