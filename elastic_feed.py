from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
def send_to_elasticsearch(items):
    # Define the Elasticsearch host and port
    es_host = 'localhost'
    es_port = 9200
    es_scheme = 'http'
    es = Elasticsearch(hosts=[{'host': es_host, 'port': es_port, 'scheme': es_scheme}])
    print (es)

    # Define the index name
    index_name = 'news_feed'

    # Define the actions for bulk indexing
    actions = []
    for item in items:
      document = {
            'title': item['title'],
            'link': item['link'],
            'pubDate': item['pubDate'],
            'description': item['description'],
            'source': item['source'],
            # Add other fields as needed
        }

        # Index the document
      es.index(index=index_name,  body=document, doc_type='doc')
      
      print(f"Indexed {item['title']}")

