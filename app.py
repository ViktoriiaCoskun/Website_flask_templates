from flask import Flask, render_template, url_for,request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/sec_page")
def sec_page():
    return render_template('sec_page.html')


@app.route("/contact_form", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
    elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

if __name__=="__main__":
    app.run(debug=True)

   # @echo off
#set FLASK_ENV=development
#flask run