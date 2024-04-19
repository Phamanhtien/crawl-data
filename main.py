import requests
import html_to_json
import json
from util import getAllATags
from util import cleanHref
from util import classify
from util import get_internal_urls

url = 'https://hasaki.vn/'
most = 'dev' # product
isGetNewData = False
CATEGORY_DATA = "categories_data.json"
HOME_PAGE = 'https://hasaki.vn'
CATEGORY = 'danh-muc'
categories_data = {}

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
        uniqueItemInCategory = list(dict.fromkeys(classifiedATags[CATEGORY]))

        # Crawling data for each category
        for i in range(0, len(uniqueItemInCategory)):
            category_link = HOME_PAGE + uniqueItemInCategory[i]
            print("Crawling data from "+category_link+" :["+i+"/"+len(uniqueItemInCategory)+"]\n")
            internal_links = get_internal_urls(category_link)
            categories_data[category_link] = internal_links

        # Storing dict to JSON file
        with open(CATEGORY_DATA, "w", encoding="utf-8") as json_file:
            json.dump(categories_data, json_file, ensure_ascii=False, indent=4)
        print("Data has saved to categories_data.json.")

            



