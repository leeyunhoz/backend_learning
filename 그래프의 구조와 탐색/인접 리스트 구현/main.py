from StationNode import *

def create_subway_graph(input_file):
    stations = {}
    
    with open(input_file) as station_raw_file:
        for line in station_raw_file:
            previous_statoin = None
            subway_line = line.strip().split("-")
            
            for name in subway_line:
                station_name = name.strip()
                
                if station_name not in stations:
                    current_station = StationNode(station_name)
                    stations[station_name] = current_station
                else:
                    current_station = stations[station_name]
                if previous_statoin is not None:
                    current_station.add_connection(previous_statoin)
                
                previous_statoin = current_station
    return stations
                    
                

stations = create_subway_graph("./stations.txt")

#station에 저장한 역 인접 역들 출력

for station in sorted(stations.keys()):
    print(stations[station])