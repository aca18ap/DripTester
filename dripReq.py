import requests as req
import random
import time
import operator
import json


start = False

headers = {'Content-Type': 'application/json'}



def createReq(job):
    data = job[0]
    url = job[1]
    print("Job request start")
    print("Creating json data")
    d = createJsonData(data)
    print(d)
    #logbox.delete('1.0',END)
    #logbox.insert('insert', str(d))
    try:
        print("Sending req to: ", url)
        print("Data: ", d)
        res = req.post(url, json=data, headers=headers, timeout=3)
        print(res)
    except:
        print("Error has occurred in the request")
        # logbox.insert(INSERT, "Request timeout\n")
    #logbox.insert(INSERT, "Server response: " + str(res.status_code) + '\n')


def createJsonData(job):
    d = json.dumps(job, indent=4).replace('"', '')
    return str(d)


