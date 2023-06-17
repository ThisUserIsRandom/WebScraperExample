from bs4 import BeautifulSoup
from urllib import request

def FindContent(sauce):
    ret = {"images":[],
            "tags":[],
            "tagsNh":[],
            "name":[]}
    url = f"https://nhentai.to/g/{sauce}/"
    htmlD = request.Request(url,headers={'User-Agent': 'RandomHuBhai'})
    soup = BeautifulSoup(request.urlopen(htmlD),'html.parser')
    images = soup.find_all('img')
    for image in images:
        if 'data-src' in image.attrs:
            ret['images'].append(str(image.attrs['data-src']))
    list1 = soup.find_all('span',{"class":"name"})
    for item in list1:
        ret['tags'].append(str(item.text))
    list2 = soup.find_all('a',{"class":"tag"})
    for item in list2:
        ret['tagsNh'].append("nhentai.to"+str(item.attrs['href']))
    ret['name'] = soup.find_all('h1')[0].text
    return ret
