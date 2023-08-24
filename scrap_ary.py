import time
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from elasticdb import send_to_elasticsearch
# url = "https://arynews.tv/category/pakistan/feed/"
# response = requests.get(url)
def ary():
    cookies = {
        'quads_browser_width': '1920',
        '_gid': 'GA1.2.1929586346.1692780981',
        '__gpi': 'UID=00000c8e831802ee:T=1692780980:RT=1692780980:S=ALNI_MbHxacHL_I-abxNr7QhC2ag2C_Klg',
        '_ga_JTDNP8EPHG': 'GS1.1.1692780980.1.1.1692780982.58.0.0',
        '_cc_id': 'f3452ff75e4febee8ac0c667cbc7d792',
        'panoramaId_expiry': '1692867381278',
        'panoramaId': '83e59562f629b52371e8e771ae5aa9fb927af85f5b41fff577f2c4dedcf0bf0f',
        'panoramaIdType': 'panoDevice',
        'quads_browser_width': '1920',
        '__gads': 'ID=979c0fa234f72d4e-22143a3c4fe0005f:T=1692780980:RT=1692780994:S=ALNI_MbuOFOqV9YOXEogeX7EFQKCCYMEWw',
        'cto_bundle': '8jMfAV9hNlpXN3VQd0dnaXZoelBOVG5EV0pyUCUyQjdqTDBlZGtSWldEZ2V5SVRCMEMwZUhjdlZyWUp6JTJCOEZnQ2RpcXJKb1hVOUhoMGdZM3I0MG41TlNBMkVna0VKZ0kwdHNtVlBSM1V4eGlUUlg0YWhoNXpQekxVYkxaeSUyQmpvViUyQkVtZDI5SGNaQXB4Ump6bnpjb201aVdGaHpOQSUzRCUzRA',
        '_hjSessionUser_1604982': 'eyJpZCI6IjIzMzY5OTk0LWEyMDctNWViNS05ZWM2LWI5YTIxZTI5NjJjYSIsImNyZWF0ZWQiOjE2OTI3ODA5OTYwMzQsImV4aXN0aW5nIjp0cnVlfQ==',
        'sc_is_visitor_unique': 'rx9464600.1692781050.BA415656DA684F7383DB907A05D14B3B.1.1.1.1.1.1.1.1.1',
        '_ga': 'GA1.1.291043387.1692780981',
        '_ga_W32PRJ2G7D': 'GS1.1.1692780995.1.1.1692781052.3.0.0',
        'FCNEC': '%5B%5B%22AKsRol8e2e4Uj-d0zxntYnkJVSf8CgMUsH2Wt7Q-y1fCpqTi0uc6ZLiUdMTJHC2QICd6xSiz266rpk1vd5BRstbCS_CDdjUcUveE39oXciuIB222L97hyMn1av0NyrvdIH52nWGQ5D7V7_IaR1DJbG86vH6D3ZbnEA%3D%3D%22%5D%2Cnull%2C%5B%5B5%2C%22534%22%5D%5D%5D',
    }

    headers = {
        'authority': 'arynews.tv',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'quads_browser_width=1920; _gid=GA1.2.1929586346.1692780981; __gpi=UID=00000c8e831802ee:T=1692780980:RT=1692780980:S=ALNI_MbHxacHL_I-abxNr7QhC2ag2C_Klg; _ga_JTDNP8EPHG=GS1.1.1692780980.1.1.1692780982.58.0.0; _cc_id=f3452ff75e4febee8ac0c667cbc7d792; panoramaId_expiry=1692867381278; panoramaId=83e59562f629b52371e8e771ae5aa9fb927af85f5b41fff577f2c4dedcf0bf0f; panoramaIdType=panoDevice; quads_browser_width=1920; __gads=ID=979c0fa234f72d4e-22143a3c4fe0005f:T=1692780980:RT=1692780994:S=ALNI_MbuOFOqV9YOXEogeX7EFQKCCYMEWw; cto_bundle=8jMfAV9hNlpXN3VQd0dnaXZoelBOVG5EV0pyUCUyQjdqTDBlZGtSWldEZ2V5SVRCMEMwZUhjdlZyWUp6JTJCOEZnQ2RpcXJKb1hVOUhoMGdZM3I0MG41TlNBMkVna0VKZ0kwdHNtVlBSM1V4eGlUUlg0YWhoNXpQekxVYkxaeSUyQmpvViUyQkVtZDI5SGNaQXB4Ump6bnpjb201aVdGaHpOQSUzRCUzRA; _hjSessionUser_1604982=eyJpZCI6IjIzMzY5OTk0LWEyMDctNWViNS05ZWM2LWI5YTIxZTI5NjJjYSIsImNyZWF0ZWQiOjE2OTI3ODA5OTYwMzQsImV4aXN0aW5nIjp0cnVlfQ==; sc_is_visitor_unique=rx9464600.1692781050.BA415656DA684F7383DB907A05D14B3B.1.1.1.1.1.1.1.1.1; _ga=GA1.1.291043387.1692780981; _ga_W32PRJ2G7D=GS1.1.1692780995.1.1.1692781052.3.0.0; FCNEC=%5B%5B%22AKsRol8e2e4Uj-d0zxntYnkJVSf8CgMUsH2Wt7Q-y1fCpqTi0uc6ZLiUdMTJHC2QICd6xSiz266rpk1vd5BRstbCS_CDdjUcUveE39oXciuIB222L97hyMn1av0NyrvdIH52nWGQ5D7V7_IaR1DJbG86vH6D3ZbnEA%3D%3D%22%5D%2Cnull%2C%5B%5B5%2C%22534%22%5D%5D%5D',
        'if-modified-since': 'Wed, 23 Aug 2023 09:13:03 GMT',
        'if-none-match': 'W/"ce03442b78ffc68b8a8f415c2ae200ef-gzip"',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    response = requests.get('https://arynews.tv/category/pakistan/feed/', cookies=cookies, headers=headers)
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
            content_encoded_element = item_element.find('.//content:encoded', namespaces={'content': 'http://purl.org/rss/1.0/modules/content/'})
            # print("content_encoded_element",content_encoded_element)
            if content_encoded_element is not None:
                content_html = content_encoded_element.text
                soup = BeautifulSoup(content_html, 'html.parser')
                
                # Extract text from <p> tags
                paragraphs = [p.get_text() for p in soup.find_all('p')]
                # print("paragraphs",paragraphs)
            else:
                paragraphs = []

            items.append({
                'title': title,
                'link': link,
                'pubDate': pub_date,
                'description': paragraphs,
                'source': 'arynews.tv',
            })

        # Print the extracted items
        # for item in items:
        #     print("Title:", item['title'])
        #     print("..............................................................................................")
        #     print("Link:", item['link'])
        #     print("...............................................................................................")
        #     print("PubDate:", item['pubDate'])
        #     print(".................................................................................................")
        #     print("Description:", item['description'])
        send_to_elasticsearch(items)
    
    else:
        print('Error: Could not fetch RSS feed content.')
