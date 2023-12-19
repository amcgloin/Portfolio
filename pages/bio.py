import os
from datetime import datetime

def archives(f):
    now=datetime.now()
    now=now.strftime("%m_%d_%Y")
    archive="archive/"+now+".html"
    f=str(f)
    with open(archive,"w") as out:
        out.write(f)

def remove_bio(lines):
    if "<!---bio--->" in lines:
        lines=str(lines.split("<!---bio--->")[0])+str(lines.split("<!---end bio--->")[1])
    return(lines)

def change_bio():
    print("Hello!")
    print("")
    print("Let's edit your bio. If you already have a bio, this will replace your existing one.")
    print("")
    print("Note: if you want some of your text to be italicized, bookmark that text with <i> and </i>. If you want it bolded, bookend it with <b> and </b>. Finally, place ""/n"" between paragraphs.")
    print("")
    print("Exit anytime by responding with 'cancel'")
    print("")
    header=input("What do you want your bio's header to be? ")
    if header.lower()=="cancel":
        return
    bio=input("Enter your bio here: ")
    if bio.lower()=="cancel":
        return
    bio=bio.replace("/n","<br><br>")
    with open("index.html","r") as f, open("edited.html","w") as out:
        lines=f.read()
      #  print(lines)
        archives(lines)
        lines=remove_bio(lines)
        edited=lines.split('</h1>')[0]+"<h2 id='bio_header'>"+header+"</h2><p id='bio_text'>"+bio+"<p>"+"<h1>Reviews</h1>"+lines.split("</h1>")[1]
        out.write(edited)
    os.rename("edited.html","index.html")
    
change_bio()

