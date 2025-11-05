import sys
import argparse
import os
import re
from ruamel.yaml import YAML
import re
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import frontmatter
from urllib.parse import urlparse

import json

url_base = "https://api.fairsharing.org/" # FAIRsharing PRODUCTION API
#url_base = "https://dev-api.fairsharing.org/" # FAIRsharing DEV API


def process_args():
    '''parse command-line arguments
    '''

    parser = argparse.ArgumentParser(prog='Tools Validator',
                                     description='This script will convert the tool and resources table to a yaml file while injecting bio.tools and FAIRsharing IDs where needed.',)
    parser.add_argument('--username',
                        help='Specify the FAIRsharing username')

    parser.add_argument('--password',
                        help='Specify the FAIRsharing password')

    parser.add_argument('--reg',
                        default=False,
                        action="store_true",
                        help='Enable TeSS, bio.tools and FAIRsharing lookup')

    args = parser.parse_args()

    return args


def get_fairsharing_token(username, password):
    url = "https://api.fairsharing.org/users/sign_in"
    payload = "{\"user\": {\"login\":\"" + username + \
        "\",\"password\":\"" + password + "\"} }"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.json()["success"] != True:
            sys.exit()
        else:
            return response.json()["jwt"]
    except:
        print("Could not login into FAIRsharing")


headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}


args = process_args()
if args.reg:
    fairsharing_token = get_fairsharing_token(args.username, args.password)
payload = "{\"user\": {\"login\":\"" + username + \
    "\",\"password\":\"" + password + "\"} }"
response = requests.request("POST", url_base+"users/sign_in", headers=headers, data=payload)
data = response.json()
jwt = data['jwt']
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': "Bearer {0}".format(jwt),
}

#All the records in FAIRsharing using the API
response = requests.request("GET", url_base+"fairsharing_records/?page[size]=1", headers=headers) #10000 for full set

if response.ok:
    all_records = json.loads(response.text)['data']
    file_records = open('../data/fairsharing_records.json', "w")
    file_records.write(json.dumps(all_records, indent=4, sort_keys=True))
    file_records.close()
    sys.exit()
else:
    print("Error")
    print(response.text)
