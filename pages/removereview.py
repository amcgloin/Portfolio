from datetime import datetime

def archives(lines):
    now=datetime.now()
    now=now.strftime("%m_%d_%Y")
    archive="archive/"+now+".html"
    f=str(lines)
    with open(archive,"w") as out:
        out.write(f)


def remove_review():
    print("")
    print("Let's delete a review. The deleted review will be stored in your archives folder.")
    print("")
    book=input("What is the name of the book you want to delete a review of? " )
    with open("index.html","r") as f, open("edited.html","w") as out:
        lines=f.read()
        archives(lines)
        tag='<h5> <a href="#'+book+'"><i>'+book+'</i> by '
        author=lines.split(tag)[1].split("</a></h5>")[0]
        full_jumpline=tag+author+"</a></h5>"
        lines=lines.replace(full_jumpline,"")
        reviews=lines.split("<h3 id=")
        new_site=[]
        header='<h3 id="'+book
        count=0
        for review in reviews:
            if count!=0:
                review="<h3 id="+review
            count=1
            if header in review:
                continue
            new_site.append(review)
        code=""
        for section in new_site:
            code+=section
        #edited=lines.split(header)[0]#+lines.split(header)[1].split()[1]
        os.rename("edited.html","index.html")
        out.write(code)


lines=remove_review()
