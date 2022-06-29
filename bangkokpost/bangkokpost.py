# import requests
# from lxml import etree
#
# url = 'https://movie.douban.com/subject/26611804/'
#
# headers ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
#
# data = requests.get(url, headers = headers).text
# s = etree.HTML(data)

import requests

proxies = {
    'https': 'https://127.0.0.1:12345',
    'http': 'http://127.0.0.1:12345'
}
# url = 'https://chengjun.github.io/mybook/04-crawler-douban.html'
# url = 'https://search.bangkokpost.com/search/result?start=10&q=china&category=all&refinementFilter=&sort=newest&rows=10'
url = 'https://search.bangkokpost.com/'
r = requests.get(url,proxies = proxies)

# r = requests.get(url)

print(r.status_code)