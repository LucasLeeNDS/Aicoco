import feedparser

def rss():
    file = feedparser.parse('https://www.bangkokpost.com/digitalproduct/rss')
    for i in file.entries:
    	print(i.title,'：',i.link)
