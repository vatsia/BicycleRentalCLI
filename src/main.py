import math
import sys
from api.digitransit import DigiTransit


def run():
    mode = None
    url = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"
    api = DigiTransit(url)

    if get_arg_value("--mode", sys.argv) is None:
        mode = "get_all_bike_stations"
    else:
        mode = get_arg_value("--mode", sys.argv)

    if mode == "get_all_bike_stations":
        res = api.get_all_bike_rental_stations()
        if is_arg_set("--filter", sys.argv):
            res["data"]["bikeRentalStations"] = filter_bike_stations(
                res["data"]["bikeRentalStations"],
                get_arg_value("--filter", sys.argv)
            )
        print("Station ID\tStation name")
        for station in res["data"]["bikeRentalStations"]:
            print(f'{station["stationId"]}\t{station["name"]}')
    elif mode == "get_bike_station_details":
        station_id = get_arg_value("--stationId", sys.argv)
        res = api.get_bike_station_details(station_id)
        make_rental_bike_station_details_readable(res["data"]["bikeRentalStation"])
    elif mode == "plan_route":
        from_place = get_arg_value("--fromPlace", sys.argv)
        to_place = get_arg_value("--toPlace", sys.argv)
        res = api.plan_route(from_place, to_place)
        make_route_plan_readable(res["data"]["plan"])
    else:
        usage()


def is_arg_set(arg_name: str, args_list: list):
    try:
        args_list.index(arg_name)
        return True
    except ValueError:
        return False


def get_arg_value(arg_name: str, args_list: list):
    if is_arg_set(arg_name, args_list):
        index = args_list.index(arg_name)
        if len(args_list) <= index + 1:
            return None
        if len(args_list[index + 1]) > 0:
            return args_list[index + 1]
    return None


def filter_bike_stations(stations: dict, keyword: str):
    return [x for x in stations if keyword in x["stationId"] or keyword in x["name"]]


def make_rental_bike_station_details_readable(station_details: dict):
    print(f'Station ID:\t {station_details["stationId"]}')
    print(f'Name:\t {station_details["name"]}')
    print(f'Bikes available:\t {station_details["bikesAvailable"]}')
    print(f'Spaces available:\t {station_details["spacesAvailable"]}')
    print(f'Latitude:\t {station_details["lat"]}')
    print(f'Longitude:\t {station_details["lon"]}')
    print(f'Dropoff Allowed:\t {station_details["allowDropoff"]}')


def make_route_plan_readable(route: dict):
    types = {"WALK": "Walking", "BICYCLE": "Cycling"}
    print("Transportation types and distances on the route")
    for itinerary in route["itineraries"]:
        for leg in itinerary["legs"]:
            print(f'Go {math.floor(leg["distance"])} meters by {types[leg["mode"]]} (Duration: {math.floor(int(leg["duration"]) / 60)} minutes)')


def usage():
    print("RentalBikeCLI v. 0.0.1")
    print("Usage: python main.py --mode <mode> [alternative args]")
    print("Please refer README.md -file for further information")


if __name__ == '__main__':
    run()

 