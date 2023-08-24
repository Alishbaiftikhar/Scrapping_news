import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from elasticdb import send_to_elasticsearch
url="https://www.geo.tv/rss/1/1"
response = requests.get(url)
print(response.status_code)
if response.status_code == 200:
    rss_xml_data = response.content
    # print(rss_xml_data)
    # Parse the XML
    rss_root = ET.fromstring(rss_xml_data)
    items = []
    for item_element in rss_root.findall('channel/item'):
        title = item_element.find('title').text
        link = item_element.find('link').text
        pub_date = item_element.find('pubDate').text
        description_element = item_element.find('description')
        if description_element is not None:
            description_html = description_element.text
            description_soup = BeautifulSoup(description_html, 'html.parser')
            for img_tag in description_soup.find_all('img'):
                img_tag.extract()
            description = description_soup.get_text().strip()
        else:
            description = ""
        items.append({
            'title': title,
            'link': link,
            'pubDate': pub_date,
             'description': description,
        })

    # for item in items:
    #     print("Title:", item['title'])
    #     print("Link:", item['link'])
    #     print("PubDate:", item['pubDate'])
    #     print("Description:", item['description'])
    #     print(".................................................................................................")
    send_to_elasticsearch(items)