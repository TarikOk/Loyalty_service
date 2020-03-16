import requests

def balance():
    response = requests.get('http://127.0.0.1:8000/api/v1/accounting/client/all/')
    response = response.json()
    point = 0
    for i in range(0, len(response)):
        point = point + response[i]['points']
    return point

def control_balance():
    response = requests.get('http://127.0.0.1:8000/api/v1/accounting/client/all/')
    response = response.json()
    for i in range(0, len(response)):
        if response[i]['points'] >=1000 or response[i]['points'] == 0:
            print ('ID = ' + str(response[i]['id']) + ', \
                    Name = ' + str(response[i]['name']) + ', \
                    Points = ' + str(response[i]['points']))
        else:
            continue