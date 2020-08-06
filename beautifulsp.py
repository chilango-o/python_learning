from bs4 import BeautifulSoup
import requests
import json

res = requests.get(
    'https://computacion.mercadolibre.com.mx/teclados-mouses-fisicos/k380')
soup = BeautifulSoup(res.text, 'lxml')

result_list = soup.find('section', {'class': 'results stack'})

items = result_list.find_all('li', {'class': 'results-item'})

 #myDict = {}

for item in items:
    title = item.select(".main-title")
    #print(type(title))
    for item in title:
        print(item.text, '\n')

""" for item in items:
    #MLMid = item.find('div', {'class': 'item'})
    item_url = item.find('div', {'class': 'images-viewer'})
    print(item_url['item-id'])
    title = item.find('span', {'class': 'main-title'})
    print(title.text)
    price = item.find('span', {'class': 'price__fraction'}).text
    num_price = int(price.replace(',', ""))
    print(num_price)
    print(item_url['item-url'])
    #myDict.update({item_url['item-id']: {'price': num_price, 'title': title.text, 'item-link': item_url['item-url']}}) """
#print(myDict)

""" with open('list.json', 'w') as write_file:
    json.dump(myDict, write_file)

print('json object saved')
print('...')
print('loading json object')

with open('list.json', 'r') as read_file:
    newDict = json.load(read_file)

print(newDict)
print() """