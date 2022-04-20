import boto3

table = boto3.resource('dynamodb').Table('FreeAwsLabsTable')

results = []

scan = table.scan()
with table.batch_writer() as batch:
    for i in scan['Items']:
        results.append([i['lab_name'], i['url']])

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