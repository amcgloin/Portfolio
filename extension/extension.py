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
            <img decoding="async" alt="CalMatters" src="https://i0.wp.com/calmatters.org/wp-content/uploads/2019/07/calmatters-logo_2x.png?fit=488%2C82&amp;ssl=1" class="i-amphtml-fill-content i-amphtml-replaced-content">
		</header>
<section class="cf w-100">
"""

article_sections=   """<article>
    <div>
    <a href="{link_}">
      <img class="article_photo" style="background-image:url({photo_});"/>
      <h3>{headline_}</h3> </a>
    </div>

  </article>"""

end="""</section>
</body>
</html>
""" 

def find_story_info(item):
    headline=item.find("title").get_text()
    link=item.find("link").get_text()
    if item.find("thumbnail"):
        photo=item.find("thumbnail")['url'].split("?")[0]
    else:
        return(headline,link,"no photo")
  #  print(photo)
   # photo=item.split('/jpeg" url="')#[1]#.split("?")[0]
    #print(photo)
    #photo=str(item.find("description")).split('src="')[1].split("?")[0]
    return(headline,link,photo)

def grab_info():
    page = fetch_page("https://calmatters.org/feed/?partner-feed=aidan")
    if not page: 
        return
    #the "soup" is the result of parsing the page with beautifulsoup's html parser. BeautifulSoup is a web scraping library
    soup = BeautifulSoup(page.content, 'xml')
   # print(soup)
    html=head
    count=10
    for item in soup.find_all("item"):
     #   print(item)
        headline,link,photo=find_story_info(item)
        if photo == "no photo":
            continue
        new_article_section=article_sections.format(link_=link,photo_=photo,headline_=headline)
        html=html+new_article_section
        if count==10:
            print(new_article_section)
            count=11
    html=html+end
    with open("newtabs.html","w") as f:
        f.write(html)

grab_info()