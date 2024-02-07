import requests
import json

getCamsURL = "https://api.aguywhosaguy.com/api/collections/streetCams/records"
dataJSON = "streetCams.json"

def get_cams():
    try:
        items = requests.get(getCamsURL).json()['items']
        return [{'baseURL': item['baseURL'], 'nickname': item["nickname"]} for item in items]
    except:
        raise Exception("Database failed to return")

def cam_gen():
    with open(dataJSON, 'w') as jsonFile:
        jsonFile.write(json.dumps(get_cams(), indent=1))

def read_json():
    try:
        with open(dataJSON, 'r') as jsonFile:
            return json.loads(jsonFile)
    except:
        return []