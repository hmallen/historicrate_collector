#!/usr/env python3

# Download GDAX level 3 order book data

import csv
import gdax
import json

public_client = gdax.PublicClient()

historic_rates = public_client.get_product_historic_rates('BTC-USD')

btcusd_data_dump = json.dumps(historic_rates)
btcusd_data = json.loads(btcusd_data_dump)

data_length = len(btcusd_data)

with open('test.csv', 'w', newline='') as csv_file:
    for x in range(0, data_length):
        for y in range(0, 5):
            csv_file.write(str(btcusd_data[x][y]))
            csv_file.write(',')
        csv_file.write(str(btcusd_data[x][5]))
        csv_file.write('\n')

"""
csv_output = csv.writer(open('test.csv', 'w', newline=''))
#csv_output = csv.writer(open('test.csv', 'w'), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

for x in btcusd_data_dump:
    csv_output.writerow([btcusd_data_dump[x][0],
                btcusd_data_dump[x][1],
                btcusd_data_dump[x][2],
                btcusd_data_dump[x][3],
                btcusd_data_dump[x][4],
                btcusd_data_dump[x][5]])

for x in btcusd_data:
    csv_output.writerow([btcusd_data[x][0],
                btcusd_data[x][1],
                btcusd_data[x][2],
                btcusd_data[x][3],
                btcusd_data[x][4],
                btcusd_data[x][5]])

print(btcusd_data[0])
print(btcusd_data[0][0])
print(btcusd_data[0][1])

for x in btcusd_data:
    csv_output.writerow([x])

print(btcusd_data)

with open('btcusd_data.json', 'w') as json_file:
        json.dump(btcusd_data, json_file, indent=4, sort_keys=True)
        
csv_output = csv.writer(open('test.csv', 'wb+'))

# Write CSV Header, If you dont need that, remove this line
#f.writerow(["pk", "model", "codename", "name", "content_type"])

for x in btcusd_ob:
    csv_output.writerow([x['time'],
                x['low'],
                x['high'],
                x['open'],
                x['close'],
                x['volume']])


x = json.loads(x)
f = csv.writer(open("test.csv", "wb+"))
"""
