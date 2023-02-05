from flask import Flask
from flask import render_template
from flask import url_for

from datetime import datetime

from forms import RegistrationForm, LoginForm



app = Flask(__name__)

app.config["SECRET_KEY"] = "8cad8d35988e98680cbb78744d628760"



posts = [
    {
        'author':'Mie Kanezaki',
        'title':'My love declaration',
        'content':'Quero casar com meu mozao ♥',
        'date_posted': str(datetime.now().date())
    },
    {
        'author':'Jane Doe',
        'title':'I am famous',
        'content':'I appear everywhere',
        'date_posted': str(datetime.now().date())

    }

]


my_var = "I love you"





# @app.route("/")
# def hello():

#     text = """
#     <h1>
#     Minha declaração ♥
#     </h1>

#     Eu amo minha princesinha linda maravilhosa
#     """

#     return text


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html",posts=posts, my_var=my_var)

@app.route("/about")
def about_page():
    return render_template("about.html", title="About")

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template("login.html", title="Login", form=form)


# RegistrationForm, LoginForm

if __name__ == "__main__":
    app.run(debug=True)


# how to run you flask app
# if you dont use app.run()
# set FLASK_APP=flask_blog.py
# set FLASK_DEBUG=1
# flask run


# to run your flask app
# type:
# python file.py



