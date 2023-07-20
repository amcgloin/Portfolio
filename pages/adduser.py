import csv

username="felix"
password="montgomery"

def check(username):
    with open("password.csv","r") as f:
        for row in csv.reader(f):
            if row[0].lower()==username.lower():
                return("already exists")

def add_username(username,password):
    if check(username)=="already exists":
        print("already exists")
        return
    with open("password.csv","a") as f:
        newrow=[username,password]
        writer=csv.writer(f)
        writer.writerow(newrow)



#add_username(username,password)

template="""<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>{user}</title>
        <meta name="description" content="">
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>{user}'s shelf</h1>
                <br><br><br>
        <footer>
        </footer>
    </body>
</html>
"""

page=template.format(user=username.title())
#print(out)

def generate_user_page(username):
    url=username+".html"
    print(url)
    with open(url,"w") as out:
        out.write(page)

#generate_user_page(username)