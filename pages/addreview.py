from datetime import datetime
import os

def archives(f):
    now=datetime.now()
    now=now.strftime("%m_%d_%Y")
    archive="archive/"+now+".html"
    with open(archive,"w") as out:
        out.write(f)

def add_review():
    print("Hello!")
    print("")
    print("Let's add a review.")
    print("")
    print("Note: if you want some of your text to be italicized, bookmark that text with <i> and </i>. If you want it bolded, bookend it with <b> and </b>. ")
    print("")
    print("Exit anytime by responding with 'cancel'")
    print("")
    book=input("What book did you read? ")
    print("")
    author=input("Who's the author? ")
    print("")
    header=input("Optional: If you want your  review to go by a different title than the book's title, enter it here. If you don't, you can just press enter: ")
    print("")
    if header.lower()=="cancel":
        return
    print("Note: you must add '/n' between paragraphs.")
    review=input("Copy your review here: ")
    review=review.replace("/n","<br><br>")
    review.replace(book,"<i>"+book+"</i>")
    if review.lower()=="cancel":
        return
    jumplink="<h5><a href='#"+book+"'><i>"+book+"</i> by "+author+"</a></h5>"
    with open("index.html","r") as f, open("edited.html","w") as out:
        lines=f.read()
        archives(f)
        lines=lines.split("<h4>Jump to a review</h4>")[0]+"<h4>Jump to a review</h4>"+jumplink+lines.split("<h4>Jump to a review</h4>")[1]
       # lines=lines.split("<h5>")[0]+jumplink+lines.split("</h5>")[1]
        if header=="":
            title="<h2 id='"+book+"'><i>"+book+"</i> by "+author+"</h2>"
        if header!="":
            title="<h2 id='"+book+"'>"+header+"</h2><h3><i>"+book+"</i> by "+author+"</h3>"
        edited=lines.split("<h1>Reviews</h1>")[0]+"<h1>Reviews</h1>"+title+"<p>"+review+"</p>"+lines.split("<h1>Reviews</h1>")[1]
        out.write(edited)

#add_review()

#os.rename("edited.html","index.html")

print("something".replace("nothing","IDEKMAN"))