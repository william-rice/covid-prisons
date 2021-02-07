import yaml
import json
import os
import requests

yaml_path = "~/covid-prisons/.census-key.yaml"

try:
    with open(os.path.expanduser(yaml_path)) as file:
        pkey = yaml.safe_load(file)
except FileNotFoundError:
    print("Cannot find file {}".format(yaml_path))

api_response = requests.get("https://api.census.gov/data/2019/pep/population?get=NAME,POP,DATE_CODE,DATE_DESC&for=state:*&key={}".format(pkey))

with open("pop_data.JSON", "w") as response_file:
        json.dump(api_response.json(), response_file, indent=4)
