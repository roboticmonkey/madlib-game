from random import choice
from random import sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']
LIBS = ['madlib.html', 'madlib2.html', 'madlib3.html']

@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)

@app.route('/game')
def show_game_form():
    """shows a game form"""

    answer = request.args.get("yesno")
    if answer == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route('/madlib',methods=["POST"])
def show_madlib():
    """Prints a madlib"""

    person = request.form.get("person")
    noun = request.form.get("noun")
    color = request.form.get("color")
    
    adj = request.form.getlist("adj")
    madlib_choice = choice(LIBS)
    


    return render_template(madlib_choice, person=person,
        noun=noun,color=color,adjectives=adj)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
