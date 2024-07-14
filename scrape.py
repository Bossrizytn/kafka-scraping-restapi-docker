import requests
from bs4 import BeautifulSoup
import json
import time
from kafka import KafkaProducer

# Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Scrape data from the website
main_url = "https://scrapeme.live/shop/"
response = requests.get(main_url)
soup = BeautifulSoup(response.content, 'html.parser')

data = []
products = soup.find_all('li', class_='product')

for product in products:
    name = product.find('h2').text
    url = main_url + name
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1', class_='product_title entry-title').text
    price = soup.find('p', class_='price').text
    description = soup.find('div', class_='woocommerce-product-details__short-description').p.text
    stock = soup.find('p', class_='stock in-stock').text
    product_data = {
        'title': title,
        'price': price,
        'description': description,
        'stock': stock
    }
    data.append(product_data)
    producer.send('product_data', value=product_data)
    time.sleep(1)

# Function to clean data
def clean_data(data):
    cleaned_data = []
    for item in data:
        cleaned_item = {
            "title": item["title"],
            "price": float(item["price"].replace("\u00a3", "").replace(",", "")),
            "description": item["description"].encode().decode('unicode_escape'),
            "stock": int(item["stock"].split()[0])
        }
        cleaned_data.append(cleaned_item)
    return cleaned_data

# Clean the scraped data
cleaned_data = clean_data(data)

# Save data to a file
with open('product_data.json', 'w') as f:
    json.dump(cleaned_data, f)
