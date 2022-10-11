import requests


class DigiTransit:

    def __init__(self, api_url: str):
        self.api_url = api_url

    def get_all_bike_rental_stations(self):
        query = """
            {
              bikeRentalStations {
                name
                stationId
              }
            }
        """
        response = requests.post(self.api_url, json={"query": query})
        return response.json()

    def get_bike_station_details(self, station_id):
        query = """
        {
          bikeRentalStation(id: "%s") {
            stationId
            name
            bikesAvailable
            spacesAvailable
            lat
            lon
            allowDropoff
          }
        }
        """ % station_id
        response = requests.post(self.api_url, json={"query": query})
        return response.json()

    def plan_route(self, from_place, to_place):
        query = """
        {
          plan(
            fromPlace: "%s"
            toPlace: "%s"
            transportModes: [{mode: BICYCLE}]
            optimize: SAFE
          ) {
            itineraries {
              legs {
                mode
                duration
                distance
              }
            }
          }
        }
        """ % (from_place, to_place)
        response = requests.post(self.api_url, json={"query": query})
        return response.json()

