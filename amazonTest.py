from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
url = 'https://www.amazon.com.mx/gp/product/B00HVLUR18/'

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.content, features="lxml")
title = soup.select("#productTitle")[0].get_text().strip()
price = soup.select("#priceblock_ourprice")[0].get_text().strip()
num_price = float(price.replace('$', '').replace(',', ''))

#textFile = open('htmlExp.txt', 'w')
#textFile.write(res.text)

print(title)
print(price)
print(num_price)