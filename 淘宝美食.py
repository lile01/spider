# encoding:utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import re
import time
from bs4 import BeautifulSoup
import pymongo

browser = webdriver.Firefox()

def search():
    try:
        browser.get("http://www.taobao.com/")
        input = browser.find_element_by_css_selector("#q")
        submit = browser.find_element_by_css_selector("#J_TSearchForm > div.search-button > button")
        input.send_keys("美食")
        submit.click()
        time.sleep(2)
        get_products()
        total = browser.find_element_by_css_selector("#mainsrp-pager > div > div > div > div.total")
        return total.text
    except TimeoutException:
        return search()
def next_page(page_number):
    try:
        current_page = browser.find_element_by_css_selector("#mainsrp-pager > div > div > div > div.form > input")
        confirm_button = browser.find_element_by_css_selector("#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")
        current_page.clear()
        current_page.send_keys(page_number)
        #browser.implicitly_wait(10)
        confirm_button.click()
        get_products()
    except TimeoutException:
        next_page(page_number)
def get_products():
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    #print(soup.prettify())
    items = soup.select("div[data-category=auctions]") + soup.select("div[data-category=personalityData]")
    # print(type(items))
    for item in items:
        #print(item)
        product = {
                "title": item.select("a[class=J_ClickStat]")[0].get_text().strip(),
                "image": item.select("div a img")[0].attrs['data-src'],
                "price": item.select("div strong")[0].get_text(),
                "deal": item.select("div [class=deal-cnt]")[0].get_text(),
                "shop": item.select("div[class=shop]")[0].get_text().strip("\n"),
                "location": item.select("div[class=location]")[0].get_text()
        }
        #print(product)
        save_mongodb(product)

def save_mongodb(result):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.spider
    table = db.taobao
    try:
        if table.insert(result):
            print("存储到mongodb成功！", result)
    except Exception:
        print("存储异常！", result)

def main():
    try:
        total = search()
        time.sleep(2)
        total = int(re.compile("(\d+)").search(total).group(1))
        for i in range(2, total+1):
            next_page(i)
            time.sleep(2)
            # get_products()
    except Exception:
        print("出错啦！")
    finally:
        browser.close()
if __name__ == "__main__":
    main()
