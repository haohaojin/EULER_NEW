import urllib3
import re

# download a web file (.html) of url with given name
def downURL(url, filename):
    try:
        fp = urllib3.urlopen(url)
    except:
        print('download exception')
        return False
    op = open(filename, 'wb')
    while True:
        s = fp.read()
        if not s:
            break
        op.write(s)

    fp.close()
    op.close()
    return True

# get urls in a web
def getURLs(url):
    try:
        fp = urllib3.urlopen(url)
    except:
        print('get url exception')
        return []
    pattern = re.compile('http://[\w\.]+')
    while True:
        s = fp.read()
        if not s:
            break
        urls = pattern.findall(s)
    fp.close()
    return urls

# crawl web in one level
def spider(startURL):
    urls = []
    urls.append(startURL)
    urllist = getURLs(startURL)
    for url in urllist:
        print(url)
        if urls.count(url) == 0:
            urls.append(url)
    i = 0
    while True:
        if len(urls) <= 0:
            break
        else:
            url = urls.pop(0)
            i = i + 1
            downURL(url, str(i) + '.html')
    return True

# test
spider('http://www.douguo.com/u/u30362766298239/recipe')