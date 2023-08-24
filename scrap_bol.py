import time
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from elasticdb import send_to_elasticsearch
def bol():
    url = "https://www.bolnews.com/politics/feed/"

    payload = {}
    headers = {
        'User-Agent': 'PostmanRuntime/7.32.3',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    # print(response.status_code)
    if response.status_code == 200:
        rss_xml_data = response.content
        print(rss_xml_data)
        # Parse the XML
        rss_root = ET.fromstring(rss_xml_data)
        items = []
        for item_element in rss_root.findall('channel/item'):
            title = item_element.find('title').text
            link = item_element.find('link').text
            pub_date = item_element.find('pubDate').text

            items.append({
                'title': title,
                'link': link,
                'pubDate': pub_date,
                'description': "",
                'source': 'bolnews.com',
            })

        # Print the extracted items
        # for item in items:
        #     print("Title:", item['title'])
        #     print("Link:", item['link'])
        #     print("PubDate:", item['pubDate'])
        send_to_elasticsearch(items)
            
    else:
        print('Error: Could not fetch RSS feed content.')
