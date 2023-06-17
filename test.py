from bs4 import BeautifulSoup
import urllib.request

def FetchEverything(page):
    url = "https://nhentai.to/?page="+page
    htmlD = urllib.request.Request(url,headers={'User-Agent': 'RandomHuBhai'})
    soup = BeautifulSoup(urllib.request.urlopen(htmlD).read(),'html.parser')
    prereq = soup.find_all("div",{"class":"container index-container"})[1]
    eligible = prereq.find_all("div",{"class":"gallery"})
    names = []
    links = []
    sauces = []
    ret = {"names" : [],
        "links" : [],
        "sauces" : [],
    }
    i = 0
    for ecchi in eligible:
        names.append(ecchi.find_all('img'))
        links.append(ecchi.find_all('div',{"class":"caption"}))
        sauces.append(ecchi.find_all('a'))
        i += 1

    for name in names:
        for sname in name:
            if "data-src" in sname.attrs:
                ret['links'].append(str(sname.attrs['data-src']))
    for link in links:
        for slink in link:
            ret['names'].append(slink.text)
    for sauce in sauces:
        for ssauce in sauce:
            ret['sauces'].append(ssauce.attrs['href'])
    return ret
