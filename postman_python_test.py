import requests

url = "https://api.clickup.com/api/v2/list/21148254/task"

payload = "{\n  \"name\": \"New Task Name\",\n}"
headers = {
  'Authorization': 'pk_4298043_IKUEXB5EFK4JIATD07Q4DGYLI0UXQYLV',
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

