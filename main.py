import requests
import html_to_json
from util import getAllATags
from util import cleanHref
from util import classify
url = 'https://hasaki.vn/'
most = 'dev' # product
isGetNewData = False
if (most == 'dev'):
    # open saving file
    with open('./data.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    isContentExist = False
    if (len(content) != 0):
        isContentExist = True
    else:
        isContentExist = False

    if (isGetNewData or isContentExist == False):
        response = requests.get('https://hasaki.vn/')
        text = response.text
        # saving file to workaround
        with open('./data.txt', 'w',  encoding='utf-8') as file:
            file.write(text)
    else:
        response = html_to_json.convert(content)
        html = response['html']
        body = html[0]['body'][0]
        aTags = []
        getAllATags(body, aTags)
        cleanHref(aTags, url)
        classifiedATags = classify(aTags)
        print(classifiedATags.keys())
            



