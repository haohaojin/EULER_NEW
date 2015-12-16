import requests
from bs4 import BeautifulSoup

with requests.session() as c:
    url = 'https://passport.douguo.com/login/?next=/'
    username = 'hao.jin@outlook.com'
    password = 'loveyou'
    c.get(url)
    login_data = dict(username=username,password=password,next='/')
    c.post(url,data=login_data)
    page = c.get('http://m.douguo.com/activity/fotilebraize/index/lists/507')
    print(page.content)
    soup = BeautifulSoup(page.text,'html.parser')

    print(soup.prettify()).encode('gb18030')

