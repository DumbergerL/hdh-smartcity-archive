import json
import requests
from datetime import datetime
from datetime import timedelta

traffic_sensor_group_identifier = 'd18db740-d364-43ff-86c7-9655d009a529'

today = (datetime.now()).strftime('%Y-%m-%d')
todayMinus7Days = (datetime.now() - timedelta(days=7) ).strftime('%Y-%m-%d')
todayMinut7DaysInFormat = todayMinus7Days + "T00:00:00.000Z"
print("Fetch dates greater or equal than: ", todayMinut7DaysInFormat)

endpoint =  "https://staging.dashboard.heidenheim.de/api/historical/?datetime__gte={0}&groupIdentifier={1}".format(todayMinut7DaysInFormat, traffic_sensor_group_identifier);

response = requests.get(endpoint)
print("Response status: ", response.status_code)

data = response.json()

fileName = 'data/{0}_{1}_Traffic.json'.format(todayMinus7Days, today)

with open(fileName, 'w') as file:
    json.dump(data, file, indent=2)
    print("Stored data in: " + fileName)