from echScrap import FindContent
from test import FetchEverything
from flask import Flask , render_template , redirect ,sessions
from flask import request as reqq
from bs4 import BeautifulSoup
import urllib.request

app = Flask(__name__,template_folder='',static_folder='')

@app.route('/')
def notMain():
    return redirect('/1')

@app.route('/<int:page>')
def mainPage(page):
    if page >=1:
        if page == 1:
            prev_button = 'secondary outline'
        else:
            prev_button = 'outline'
        data = FetchEverything(str(page))
        names = data['names']
        links = data['links']
        sauces = data['sauces']
        return render_template('main.html',
                                names=names,
                                links=links,
                                sauces=sauces,
                                page=page,
                                prev_button=prev_button)
    else:
        return redirect('/1')

@app.route('/random')
def getNew():
    url = "https://nhentai.to/random/"
    htmlD = urllib.request.Request(url,headers={'User-Agent': 'RandomHuBhai'})
    soup = BeautifulSoup(urllib.request.urlopen(htmlD).read(),'html.parser')
    heading  = str(soup.find_all("h2")[0].text.strip())
    images = str(soup.find_all("img")[2].attrs['src'])
    url = str(soup.find_all('h3')[0].text[1:])
    return render_template('Ecc.html',
                            heading=heading,
                            image=images,
                            url=url)

@app.route('/ecchi/g/<sauce>/')
def kalKarunga(sauce):
    listOfArgs = FindContent(sauce)
    return render_template("avgPage.html"
                            ,coverPhoto=listOfArgs['images'][0],
                            tags=listOfArgs['tags'],
                            Lentags=len(listOfArgs['tags']),
                            tagsNh=listOfArgs['tagsNh'],
                            sauce=sauce,
                            name=F'{listOfArgs["name"]}')

@app.route('/fetch/<sauce>')
def returnD(sauce):
    images = FindContent(sauce)['images']
    return images

@app.route('/ecchi/g/<sauce>/<page>')
def onePanel(sauce,page):
    arrayOfImages = FindContent(sauce)
    image = arrayOfImages['images']
    return render_template("onePanel.html",
                            sauce=sauce,
                            pageno=page)

@app.route('/search',methods=['GET','POST'])
def search():
    if reqq.method == 'POST':

        searchString = reqq.form['search']
        lisofKeys = searchString.split(' ')
        url = 'https://nhentai.to/search?q='+"+".join(lisofKeys)
        htmlD = urllib.request.Request(url,headers={'User-Agent': 'RandomHuBhai'})
        soup = BeautifulSoup(urllib.request.urlopen(htmlD).read(),'html.parser')

        listOsauces = []
        names = []
        images = []

        Sauces = soup.find_all('a',{'class':'cover'})
        for sauce in Sauces:
            listOsauces.append(str(sauce.attrs['href']))

        Names = soup.find_all('div',{'class':'caption'})
        for name in Names:
            names.append(str(name.text))

        Images = soup.find_all('a',{'class':'cover'})
        for image in Images:
            eachimgs = image.find_all('img')
            for eachimg in eachimgs:
                images.append(eachimg.attrs['src'])

        if len(names)>25:
            renderLen=25
        else:
            renderLen = len(names)
        return render_template('searchPage.html',
                                links=images,
                                sauces=listOsauces,
                                names=names,
                                lenFound = renderLen)


@app.route('/login')
def login():
    return "under development"

@app.route('/register')
def register():
    return "under development"


app.run(debug=True,host="192.168.100.5",port=80)
