import sys
import os 
import requests
import json


def main(name):
    url = "https://api.github.com/user/repos"

    token = "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"


    username = "Yurnero99"

    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }

    data = {

        "name": name ,
        "private" : "False" ,
    }

    res = requests.post(url, data=json.dumps(data) , headers = headers , auth =(username,token))

    ssh_uri = res.json()["ssh_url"]

    os.chdir("D:\Regular\Python Eshikhon\Local Repo")

    os.system(f'git clone {ssh_uri}')

main(sys.argv[1])

