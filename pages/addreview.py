
import csv

def review_password(username,password):
    with open("password.csv","r") as f:
        for row in csv.reader(f):
            if row[0].lower()==username.lower():
                if row[1]==password:
                    return("passed")
                else:
                    return("wrong password")

def remove_review(book,lines):
    title="<h3><i>"+book
    review=lines.split(title)[1].split("<h3><i>")[0]
    review=title+review
    lines=lines.replace(review,"")
    return(lines)


def add_review(username,password,book,author,review):
    if review_password(username,password)=="wrong password":
        print("wrong password")
        return
    url=username+".html"
   # print(url)
    with open(url,"r") as f, open("edited.html","w") as out:
        lines=f.read()
       # print(lines.split("webpage because")[0])
        title="<h3><i>"+book+"</i> by "+author+"</h3>"
        if title in lines:
            print("Review already in")
            lines=remove_review(book,lines)
        edited=lines.split("<h2>Reviews</h2>")[0]+"<h2>Reviews</h2>"+title+"<p>"+review+"</p>"+lines.split("<h2>Reviews</h2>")[1]
        print(lines.split("<h2>Reviews</h2>")[0])
        out.write(edited)

#os.rename("edited.html",url)

#add_review("aidan","test","If This Isn't Nice, What Is?","Kurt Vonnegut","sdfdsfsd")