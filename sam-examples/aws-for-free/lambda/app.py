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

# render returned HTML file
from yattag import Doc
from yattag import indent

doc, tag, text = Doc().tagtext()

with tag('html'):

    with tag('head'):
        with tag('link'):
            doc.attr(href='https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css', rel="stylesheet")
            
    with tag('body'):
        with tag('h1', klass="container p-3 my-3 border bg-warning d-flex justify-content-center rounded shadow"):
            text(f'FREE AWS labs')

        with tag('h4', klass="container mt-4 mb-1"):
            text(f'Links:')

        with tag('table', klass="container table"):
            for idx, item in enumerate(results):
                with tag('tbody'):
                    with tag('tr'):
                        with tag('th', scope="row"):
                            text(f"#{idx+1}")
                        with tag('td'):
                            with tag('a', href=item[1]):
                                text(item[0])

        with tag('script'):
            doc.attr(src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js")


def lambda_handler(event, context):
      
    return {
        "statusCode": 200,
        "body": indent(
            doc.getvalue(),
            indentation = '    ',
            newline = '\n',
            indent_text = True
        ),
        "headers": {
            "Content-Type": "text/html"
        },
    }        