
def start_site():
    name=input("What do you want to name your site? ")
    print("")
    if name.lower()=="cancel":
        return
    title=input("What do you want the top header to say? ")
    print("")
    goodreads_link=input("What is the link to your GoodReads? Press enter if you want to skip. ")
    print("")
    goodreads="<a href="+goodreads_link+">Goodreads</a>| "
    if goodreads_link=="":
        goodreads=""
    instagram_link=input("What is the link to your Instagram? Press enter if you want to skip. ")
    instagram="<a href="+instagram_link+">Instagram</a>| "
    if instagram_link=="":
        instagram=""
    print("")
    twitter_link=input("What is the link to your Twitter? Press enter if you want to skip. ")
    twitter="<a href="+twitter_link+">Twitter</a>| "
    if instagram_link=="":
        twitter=""
    print("")
    facebook_link=input("What is the link to your Facebook? Press enter if you want to skip. ")
    facebook="<a href="+facebook_link+">Facebook</a>|"
    if facebook_link=="":
        facebook=""
    text="""
<!DOCTYPE html>
<html>
    
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>"""+name+""""</title>
        <meta name="description" content="For readers.">
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
    <h1 id="header">"""+title+"""</h1>
            <!---bio--->
            <!---end bio--->
       <footer>
        <b>Contact| </b>"""+goodreads+instagram+twitter+facebook+"""
        </footer>
    </body>
</html>"""
    with open("index.html","w") as f:
        f.write(text)
    print("Congratulations! The basic structure of your website is complete.")
    print("")
    print("Now run 'python3 bio.py' to add a little about you, or skip straight ahead to 'python3 addreview.py' if you want to start publishing your thoughts on books.")

start_site()