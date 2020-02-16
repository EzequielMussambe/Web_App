from flask import Flask, render_template, request
import datetime

app=Flask(__name__)

@app.route("/")

# # Looping through items
# def index():
#     names=["pedro", "john", "alice", "bob"]
#     return render_template("index.html", names=names)

# CHANGE BETWEEN PAGES
def index():

    return render_template("index.html")

#@app.route("/hello", methods=["POST"])

# def hello():
#     name=request.form.get("name")
#     return render_template("hello.html", name=name)
# def more():
#     return render_template("more.html")

# CONDITIONAL STATEMENTS
# def index():
#     now=datetime.datetime.now()
#     new_year=now.month==1 and now.day==1
#     new_year=True# if we want to display the new year messages
#     return render_template("index.html", new_year=new_year)
#===========================================================
#RENDORING WITH STRING
# def index():
#     return "Hello, World22222"

# @app.route("/David")

# def devid():
#     return "Hello David"

#@app.route("/<string:name>")#this will receive the name.
#================================================================

#USING HTML TO RENDORING
# def index():
    #name=name.capitilize()
    #return f"<h1>Hello {name}</h1>"
    # headline="Hello Forty"
    # return render_template("index.html", headline=headline) 
    #headline will render the headline to the html inside of hmtl we will use 
    #{{headline}} inside of the body
    # the index,html must be under folder call templates

#REPLACE INFO AT HTML
# @app.route("/bye")

# def devid():
#     headline="BYEGOODFRIEND"
    #return render_template("index.html", headline=headline)
#===============================================================
# if __name__ == "__main__":
#     app.run(debug=True)
    # i solved the debug mode problem by rum
    #set FLASK_ENV=development: see link: https://stackoverflow.com/questions/51025893/flask-at-first-run-do-not-use-the-development-server-in-a-production-environmen