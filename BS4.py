# encoding:utf-8
import requests
from requests.exceptions import RequestException
import re
import json
from bs4 import BeautifulSoup
import xlwt


def get_one_page(url):
    try:
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None
'''
def parse_one_page(html):
    pattern = re.compile("<dd>.*?board-index.*?>(\d+)</i>.*?data-src=\"(.*?)\".*?class=\"name.*?title=\"(.*?)\".*?"
                         "star\">(.*?)</p>.*?releasetime\">(.*?)</p>.*?integer\">(.*?)</i>.*?fraction\">(.*?)</i>.*?</dd>", re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {
            "index": item[0],
            "images": item[1],
            "title": item[2],
            "actor": item[3].strip()[3:],
            "time": item[4].strip()[5:],
            "score": item[5]+item[6]
        }
'''
def bs4_one_page(html):
    soup = BeautifulSoup(html, "lxml")
    content = soup.find_all('dd')
    items = []
    for c in content:
        #item = {}
        name = c.select('a')[0].attrs['title']
        index = c.select('i')[0].get_text()
        actor = c.find_all('p', class_='star')[0].get_text().strip('\n').strip()
        time = c.select('p[class=releasetime]')[0].get_text()
        score = c.select('p i[class=integer]')[0].get_text() + c.select('p i[class=fraction]')[0].get_text()
        image = c.select('a img[class=board-img]')[0].attrs['data-src']
        #print(index)
        #print(name)
        #print(actor[3:])
        #print(time[5:])
        #print(score)
        #print(image)
        for i in (index,name,actor,time,score):
            print(items.append(i))

        #items += items.append(i)

        #return items
'''
def write_file(index, name, actor, time, score):
        with open('top.txt','a+', encoding='utf-8') as f:
            f.write(index + '  ' + name + '  ' + actor + '  ' + time + '  ' + score + '       ' + image + '  ' + '\n')
            f.close()
'''
def write_excel(content):
        newTable = '电影TOP10.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('test')
        header = ['排名', '电影', '主演', '上映时间','评分']
        for c in range(len(header)):
            ws.write(0, c, header[c])
        index = 1
        for item in content:
            print(item)
            for i in range(0, 5):
                ws.write(index, i, item[i])
            index += 1
            wb.save(newTable)




def write_to_file(content):
    with open("result.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(content, ensure_ascii=False) + "\n" )
        f.close()
'''
def excel_write(cont):
    newTable = "output.xls"
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("test1")
    headData = ['排名', '影片', '图片地址', '主演', '上映时间', '评分']
    for colnum in range(0, 6):
        ws.write(0, colnum, headData[colnum], xlwt.easyfont('font: bold on'))
    wb.save(newTable)
'''

def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    # print(html)
    content = bs4_one_page(html)
    write_excel(content)
    #parse_one_page(html)
    #for item in parse_one_page(html):
        #print(item)
    #write_file(index, name, actor, time, score)
    #write_excel(index,name,actor,time,score)

if __name__ == "__main__":
    for i in range(10):
        main(i*10)
