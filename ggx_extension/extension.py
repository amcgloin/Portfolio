from os import write
import requests
from bs4 import BeautifulSoup

#This is a fail-safe to make sure I get responses from my scraping. If I don't open a page or if there is a time-out, I exit and move to the next url
def fetch_page(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}
    page = requests.get(url.rstrip(),headers = headers)
    return page

head="""
<html>
<head>
    <link href="extension.css" rel="stylesheet" type="text/css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700&display=swap" rel="stylesheet">
</head>
   <body>
		<header class="bb pv4">
            <img class="headerphoto" decoding="async" alt="Golden Gate Xpress wordmark" src="https://goldengatexpress.org/wp-content/uploads/2020/08/xpress_newsmag_header-e1598390074185.png" class="i-amphtml-fill-content i-amphtml-replaced-content">
		</header>
<section class="cf w-100">
"""

article_sections=   """<article>
    <div>
    <a href="{link_}" target="_top">
      <img class="article_photo" style="background-image:url({photo_});"/>
      <h3>{headline_}</h3> </a>
    </div>

  </article>"""

end="""</section>
</body>
</html>
""" 

def find_photo(link):
    page=fetch_page(link)
    soup=BeautifulSoup(page.content,"html.parser")
    body=soup.find("div",id="storypage")
    photo=body.find("img")
    print(photo)
    return(photo)

def find_story_info(item):
    headline=item.find("title").get_text()
    link=item.find("link").get_text()
    print(headline)
    print(link)
    photo=find_photo(link)["src"]
    print("#")
    print(photo)
    print("#")
    return(headline,link,photo)

def grab_info():
    page = fetch_page("https://goldengatexpress.org/feed/")
    if not page: 
        return
    #the "soup" is the result of parsing the page with beautifulsoup's html parser. BeautifulSoup is a web scraping library
    soup = BeautifulSoup(page.content, 'xml')
   # print(soup)
    html=head
    for item in soup.find_all("item"):
     #   print(item)
        headline,link,photo=find_story_info(item)
        if photo == "no photo":
            continue
        new_article_section=article_sections.format(link_=link,photo_=photo,headline_=headline)
        html=html+new_article_section
    html=html+end
    with open("ggx_extension/newtabs.html","w") as f:
        f.write(html)

grab_info()
