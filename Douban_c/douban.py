from IPython.core.display import HTML
from IPython.display import display
import requests
from requests.structures import CaseInsensitiveDict
from lxml import etree

url = "https://book.douban.com/tag/%E7%BC%96%E7%A8%8B"

headers = CaseInsensitiveDict()

headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["Referer"] = "https://book.douban.com/"

resp = requests.get(url, headers=headers)

content = resp.text
sel = etree.HTML(content)

for block in sel.xpath('//li[@class="subject-item"]'):
    title = ''
    elem_title = block.xpath('.//h2/a')
    if elem_title:
        title = ''.join(elem_title[0].itertext()).replace(' ','').replace('\n','')
    print(title)

    price = -1
    elem_price = block.xpath('.//span[@class="buy-info"]/a/text()')
    if elem_price:
        price = float(elem_price[0].strip()[3:-1])
    print(price)

    cover = ""
    elem_cover = block.xpath(".//img/@src")
    if elem_cover:
        cover = elem_cover[0]
    display(HTML(f"<img src='{cover}'>"))