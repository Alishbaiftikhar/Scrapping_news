from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import spacy

nlp = spacy.load("en_core_web_sm")

def is_duplicate_item(existing_title, existing_source, new_title, new_source, similarity_value=0.85):
    title_similarity = nlp(existing_title).similarity(nlp(new_title))
    source_similarity = nlp(existing_source).similarity(nlp(new_source))
    return title_similarity >= similarity_value and source_similarity >= similarity_value
def send_to_elasticsearch(items):
#   import pdb; pdb.set_trace()
  es_host = 'localhost'
  es_port = 9200
  es_scheme = 'http'
  es = Elasticsearch(hosts=[{'host': es_host, 'port': es_port, 'scheme': es_scheme}])
#   print (es)
  index_name = 'news_feed'
  actions = []
  for item in items:
        # Check if a similar title and source exist in the index
        # import pdb; pdb.set_trace()
        is_duplicate = False
        query = {
    'query': {
        'bool': {
            'must': [
                {'match': {'title': item['title']}},
                {'match': {'source': item['source']}}
            ]
        }
    }
}
        search_results = es.search(index=index_name, body=query)
        print(search_results)
        for hit in search_results['hits']['hits']:
            existing_title = hit['_source']['title']
            existing_source = hit['_source']['source']
            if is_duplicate_item(existing_title, existing_source, item['title'], item['source']):
                is_duplicate = True
                break
        
        if is_duplicate:
            print(f"Data for '{item['title']}' and '{item['source']}' is a duplicate. Skipping.")
            print("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
            continue
        if not is_duplicate:
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
