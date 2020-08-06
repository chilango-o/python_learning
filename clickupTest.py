import requests, time, calendar

token = "pk_4298043_IKUEXB5EFK4JIATD07Q4DGYLI0UXQYLV"
makermed_space_ID = '6328067'
team_ID = '2252310'
makermed_desarrollo_list_ID = '21148254'
ismael_ID = '4298043'
darius_ID = '4297800'

def makelist():
    calTime = (calendar.timegm(time.gmtime())) * 1000
    post = requests.post(
        f'https://api.clickup.com/api/v2/list/{makermed_desarrollo_list_ID}/task',
        headers={'Authorization': token},
        data={
            "name": "test task",
            "description": "New Task Content, where's description?",
            "assignees": [
                4298043
            ],
            "status": "Open",
            "priority": 3,
            "due_date": 1593277200000,
            "due_date_time": True,
            "time_estimate": 8640000,
            "start_date": 1593137062000,
            "start_date_time": True,
            "notify_all": True,
        }
        
    )
    print(post.text)

def getSpaces():
    response = requests.get(
            f'https://api.clickup.com/api/v2/team/{team_ID}/space?archived=false',
            headers={'Authorization': token}
        )

    responseDict = response.json()
    for space in responseDict.values():
        for name in space:
            print(name['id'], name['name'])
    
def getList():
    response = requests.get(
        f'https://api.clickup.com/api/v2/space/{makermed_space_ID}/list?archived=false',
        headers={'Authorization': token}
        )
    responseDict = response.json()
    for space in responseDict.values():
        for name in space:
            print(name['id'], name['name'])

def getMembers():
    response = requests.get(
    f'https://api.clickup.com/api/v2/list/{makermed_desarrollo_list_ID}/member',
    headers = {'Authorization': token}
    )
    responseDict = response.json()
    for space in responseDict.values():
        for name in space:
            print(name['id'], name['username'])

makelist()