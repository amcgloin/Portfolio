from datetime import datetime
from prompt_toolkit import prompt

def archives(url,f):
    now=datetime.now()
    now=now.strftime("%m_%d_%Y")
    archive="archive/"+now+".html"
    f=str(f)
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
    url ="index.html"
    book=prompt("What book did you read? ")
    print("")
    author=prompt("Who's the author? ")
    print("")
    header=prompt("Optional: If you want your  review to go by a different title than the book's title, enter it here. If you don't, you can just press enter: ")
    print("")
    if header.lower()=="cancel":
        return
    review=prompt("Copy your review here (note: you must add ""/n"" between paragraphs):  ")
    review=review.replace("/n","<br><br>")
    if review.lower()=="cancel":
        return
    jumplink="<h5><a href='#"+book+"'><i>"+book+"</i> by "+author+"</a></h5>"
    with open(url,"r") as f, open("edited.html","w") as out:
        lines=f.read()
        archives(url,lines)
        print(lines.split("<h5>")[0])
        print("#######")
        print(lines.split("<h5>")[1])
        lines=lines.split("<h4>Jump to a review</h4>")[0]+jumplink+lines.split("<h4>Jump to a review</h4>")[1]
       # lines=lines.split("<h5>")[0]+jumplink+lines.split("</h5>")[1]
        if header=="":
            title="<h2 id='"+book+"'><i>"+book+"</i> by "+author+"</h2>"
        if header!="":
            title="<h2 id='"+book+"'>"+header+"</h2><h3><i>"+book+"</i> by "+author+"</h3>"
        edited=lines.split("<h1>Reviews</h1>")[0]+"<h1>Reviews</h1>"+title+"<p>"+review+"</p>"+lines.split("<h1>Reviews</h1>")[1]
        out.write(edited)

os.rename("edited.html",url)

add_review()


