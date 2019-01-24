"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():

    play_game = request.args.get("wants_game")

    # if yes, render_template("game.html")
    if play_game == "Yes":
        return render_template("game.html")
    # if no, render_template("goodbye.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib', methods=["POST"])
def show_madlib():

    color = request.form.get("color")
    noun = request.form.get("noun")
    person = request.form.get("person")

    adjective = []
    adjective1 = request.form.get("adjective1")
    print(adjective1)
    if adjective1:
        adjective.append(adjective1)
    adjective2 = request.form.get("adjective2")
    print(adjective2)
    if adjective2:
        adjective.append(adjective2)
    adjective3 = request.form.get("adjective3")
    print(adjective3)
    if adjective3:
        adjective.append(adjective3)


    # # adjective = request.args.get("adjective")
    print(adjective)

    return render_template("madlib.html", color=color, noun=noun, person=person.title(), adjective=adjective)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
