import csv

def review_password(username,password):
    with open("password.csv","r") as f:
        for row in csv.reader(f):
            if row[0].lower()==username.lower():
                if row[1]==password:
                    return("passed")
                else:
                    return("wrong password")

def remove_bio(lines):
    if "<!---bio--->" in lines:
        lines=lines.split("<!---bio--->")[0]+lines.split("<!--end bio--->")
    return(lines)

def add_bio(username,password,header,bio):
    if review_password(username,password)=="wrong password":
        print("wrong password")
        return
    url=username+".html"
    with open(url,"r") as f, open("edited.html","w") as out:
        lines=f.read()
        lines=remove_bio(lines)
        edited=lines.split("</h1>")[0]+"</h1><!---bio---><h2>"+header+"</h2><p>"+bio+"</p><!---end bio---><h2>Reviews<h2>"+lines.split("<h2>Reviews")[1]
        out.write(edited)

add_bio("Aidan","test","My life","I was born and raised in...")