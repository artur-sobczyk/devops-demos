import requests
import logging
from bs4 import BeautifulSoup
import boto3

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
xray_recorder.configure()

logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()

url = 'https://amazon.qwiklabs.com/catalog'

# find tuples wtih free resources in html file
@xray_recorder.capture('## find_free_entries')
def find_free_entries(url):

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    elements = soup.find_all('div', attrs={'class': 'catalog-item'})

    list = []

    for e in elements:
        if "Free" in e.text: 
            list.append((e.h3.a.text, 'https://amazon.qwiklabs.com' + e.h3.a['href']))

    return list

def lambda_handler(event, context):

    results = []
    
    # iterate over all pages with labd in catalogs
    for i in range(1,14):
        if(i == 1):
            req_url = url
        else:
            req_url = url + f"?page={i}"

        results.extend(find_free_entries(req_url))


    # Get the service resource.
    table = boto3.resource('dynamodb').Table('FreeAwsLabsTable')
    
    scan = table.scan()

    if scan['Count'] > 0:
        with table.batch_writer() as batch:
            for i in scan['Items']:
                batch.delete_item(Key={'lab_name': i['lab_name']})

    for i in results:
        table.put_item(Item = {
            'lab_name': i[0],
            'url': i[1],
        })