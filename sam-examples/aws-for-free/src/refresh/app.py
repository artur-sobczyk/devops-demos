import requests
from bs4 import BeautifulSoup

url = 'https://amazon.qwiklabs.com/catalog'

# find tuples wtih free resources in html file
def find_free_entries(url):

    #print(f"url - {url}")

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    elements = soup.find_all('div', attrs={'class': 'catalog-item'})

    list = []

    for e in elements:
        if "Free" in e.text: 
            list.append((e.h3.a.text, 'https://amazon.qwiklabs.com' + e.h3.a['href']))

    return list

results = []

# iterate over all pages with labd in catalogs
for i in range(1,14):
    if(i == 1):
        req_url = url
    else:
        req_url = url + f"?page={i}"

    results.extend(find_free_entries(req_url))

def lambda_handler(event, context):

    import boto3

    # Get the service resource.
    table = boto3.resource('dynamodb').Table('FreeAwsLabsTable')
    
    scan = table.scan()
    with table.batch_writer() as batch:
      for i in scan['Items']:
        batch.delete_item(Key=i)

    for i in results:
        table.put_item(Item = {
            'lab_name': i[0],
            'url': i[1],
        })