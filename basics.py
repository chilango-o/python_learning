from bs4 import BeautifulSoup
import requests
import json

res = requests.get(
    'https://laptops.mercadolibre.com.mx/laptops-accesorios/macbook-pro-2015_OrderId_PRICE_Installments_NoInterest')
soup = BeautifulSoup(res.text, 'lxml')

result_list = soup.find('section', {'class': 'results stack'})

items = result_list.find_all('li', {'class': 'results-item'})

myDict = {}

for item in items:
    MLMid = item.find('div', {'class': 'item'})
    title = item.find('span', {'class': 'main-title'})
    price = item.find('span', {'class': 'price__fraction'}).text
    num_price = int(price.replace(',', ""))
    msi = num_price / 18
    myDict.update({int(MLMid['id'][3:]): {'price': num_price, 'title': title.text}})
print(myDict)

with open('list.json', 'w') as write_file:
    json.dump(myDict, write_file)

""" print('json object saved')
print('...')
print('loading json object')

with open('list.json', 'r') as read_file:
    newDict = json.load(read_file)

print(newDict)
print()
 """