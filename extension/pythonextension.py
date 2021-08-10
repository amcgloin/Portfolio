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
</head>
   <body>
		<header class="bb pv4">
            <img decoding="async" alt="CalMatters" src="https://i0.wp.com/calmatters.org/wp-content/uploads/2019/07/calmatters-logo_2x.png?fit=488%2C82&amp;ssl=1" class="i-amphtml-fill-content i-amphtml-replaced-content">
		</header>
<section class="cf w-100">
"""

article_sections=   """<article class="fl w-100 w-50-m  w-25-ns">
    <div class="aspect-ratio aspect-ratio--1x1">
    <a href="{link_}">
      <img style="background-image:url({photo_});" 
      class="db bg-center cover aspect-ratio--object" />
      <h3 class="f4-ns headline">{headline_}</h3> </a>
    </div>

  </article>"""

end="""</section>
</body>
</html>
""" 

def find_story_info(item):
    headline=item.find("title").get_text()
    link=item.find("link").get_text()
    photo=str(item.find("description")).split('src="')[1].split("?")[0]
    return(headline,link,photo)


def grab_info():
    page = fetch_page("https://calmatters.org/feed/")
    if not page: 
        return
    #the "soup" is the result of parsing the page with beautifulsoup's html parser. BeautifulSoup is a web scraping library
    soup = BeautifulSoup(page.content, 'xml')
   # print(soup)
    page=head
    for item in soup.find_all("item"):
       # print(item)
        headline,link,photo=find_story_info(item)
        new_article_section=article_sections.format(link_=link,photo_=photo,headline_=headline)
        page=page+new_article_section
    page=page+end
    with open("newtabs.html","w") as f:
        f.write(page)


grab_info()