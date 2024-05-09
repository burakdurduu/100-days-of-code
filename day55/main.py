from flask import Flask
from random import choice

guess = choice(range(10))
print(guess)

app = Flask(__name__)
style = '<style>body {text-align: center} a {padding:0 30px; font-size:50px; text-decoration: none;} </style>'
links = ('<br><br><br>'
         '<a href="/0">0</a>'
         '<a href="/1">1</a>'
         '<a href="/2">2</a>'
         '<a href="/3">3</a>'
         '<a href="/4">4</a>'
         '<a href="/5">5</a>'
         '<a href="/6">6</a>'
         '<a href="/7">7</a>'
         '<a href="/8">8</a>'
         '<a href="/9">9</a>')


@app.route('/')
def route():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/LcoK2zRKbQlUc/giphy.gif">' + links)


@app.route('/<int:number>')
def answer(number):
    if number < guess:
        return (style + '<h1 style="color: red"> Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/LcoK2zRKbQlUc/giphy.gif">' + links)
    elif number > guess:
        return (style + '<h1 style="color: violet"> Too hi, try again!</h1>'
                '<img src="https://media.giphy.com/media/LcoK2zRKbQlUc/giphy.gif">' + links)
    else:
        return (style + '<h1 style="color: green"> You found me!!!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')


if __name__ == '__main__':
    app.run(debug=True)
