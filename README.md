# RentalBikeCLI
RentalBikeCLI is a pretty simple command line tool for fetching data about rental bicycles and routes from DigiTraffic GraphiQL API.

## "Installation"
Application has one dependency, which can be installed with Python's package manager PIP
``pip -r src/requirements.txt``

After installation the application should be ready to be used.

## Building and running with Docker
Source code includes small Dockerfile, which enables application to be ready to be containerized.

Building image:
``docker build . -t bicycle_app``

Running container with arguments:

`` docker run bicycle_app:latest --mode get_all_bike_stations --filter eure``

## Examples
### Fetch all bike stations
This functionality fetches all the bike stations and shows their ID's. Results can be filtered with `--filter <keyword>` -option
``python src/main.py --mode get_all_bike_stations --filter eure``

Result:
```
Station ID      Station name
6dd5413c-8ea0-4c6c-8b61-7ebbc1b0b7d6    Heureka
```
### Fetch details about a bike station
This functionality fetches a little bit more information about a bike station and shows them as human readable text
``python src/main.py --mode get_bike_station_details --stationId 6dd5413c-8ea0-4c6c-8b61-7ebbc1b0b7d6``
Results:
```
Station ID:      6dd5413c-8ea0-4c6c-8b61-7ebbc1b0b7d6
Name:    Heureka
Bikes available:         11
Spaces available:        9
Latitude:        60.288622
Longitude:       25.041903
Dropoff Allowed:         True
```
### Route planning
Fetch route plan with place coordinates
``python src/main.py --mode plan_route --fromPlace 60.15978,24.91842 --toPlace 60.18204,24.92756``
Which ends up with the results of how the route could be transported:

```
Transportation types and distances on the route
Go 30 meters by Walking (Duration: 0 minutes)
Go 3181 meters by Cycling (Duration: 14 minutes)
```