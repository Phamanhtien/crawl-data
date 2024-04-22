import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

product_data = []

with open('categories_data.json') as json_file:
    data = json.load(json_file)

for category_url, product_urls in data.items():
    print("Category URL:", category_url)
    for product_url in product_urls:
        print("Product URL:", product_url)
        response = requests.get(product_url);
        soup = BeautifulSoup(response.text, 'html.parser')
        product_name = soup.find("span", class_="product__title base").text.strip()
        product_price = soup.find("span", {"id" : "product-final_price"}).text.strip()
        product_barcode = soup.find("td", class_="barcode-content").text.strip()
        product_branch = soup.find("a", class_="title-brand txt_color_1").text.strip()
        product_review_count = soup.find("div", class_="txt_total_nhanxet").text.strip()
        product_brand_origin = soup.find(string="Xuất xứ thương hiệu").parent.findNext("td").text
        product_manufacture_place = soup.find(string="Nơi sản xuất").parent.findNext("td").text 
        # Thêm dữ liệu vào danh sách
        product_data.append({
            "Tên sản phẩm": product_name,
            "Barcode": product_barcode,
            "Giá": product_price,
            "Thương hiệu": product_branch,
            "Lượt đánh giá": product_review_count,
            "Xuất xứ thương hiệu": product_brand_origin,
            "Nơi sản xuất": product_manufacture_place
        })
print("Dữ liệu đã được ghi vào tệp product_data.csv")
df = pd.DataFrame(product_data)
df.to_csv("product_data.csv", index=False, encoding="utf-8-sig")
