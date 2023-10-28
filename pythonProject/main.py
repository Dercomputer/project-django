"""
from geopy.distance import geodesic
point1 = input()
point2 = input()
distance = geodesic(point1, point2).km
print(distance)

from geopy.distance import geodesic
point1 =
point2 = input()
distance = geodesic(point1, point2).km
print(distance)
"""
from yaweather import UnitedStates, YaWeather

y = YaWeather(api_key='431c566a-318a-4429-8d51-cc9899571879')

res = y.forecast(UnitedStates.NewYork)

for f in res.forecasts:
    day = f.parts.day_short
    print(f'{f.date} | {day.temp} °C, {day.condition}')