import csv
import json
import requests

url = 'https://rest.iad-06.braze.com/users/delete'
API_KEY = 'Bearer 8fbe8e86-f74b-4e20-b1f3-72790336a69b'

headers = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
}

with open('braze_prod_cleanup.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if len(row) == 0:
            continue
        temp = row[0].split(",")
        if temp[0] == "external_id":
            continue

        body = json.dumps({"external_ids": [temp[0]]
                           })

        response = requests.post(url, data=body, headers=headers)
        print(response.json())