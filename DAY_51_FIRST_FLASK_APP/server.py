from flask import Flask
import random

NUMBER = random.randint(0, 9)
app = Flask(__name__)

def decorator_heading(func):
    def wrapper(*args, **kwargs):
        return "<h1>" + func(*args, **kwargs) + "</h1>"
    return wrapper

@app.route('/', endpoint='home')
@decorator_heading  
def home():
    return ("GUESS A NUMBER BETWEEN 0 TO 9 "
            "<br><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjczbjF1eGY4Z2pnZXRoZGJqbWc5bGd4a3k5am5rdGgxeDB1OXUweiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Kehzyp9EFa2IYDte8P/giphy.gif' />")

@app.route('/<int:id>', endpoint='guess')
@decorator_heading
def guess(id):
    if id == NUMBER:
        return ("You guessed the right number "
                "<br><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdG04bzUzNnFobGRqenFtb201aDN1N3p0NHFhY3MwMTNtOXQ0M2E3MCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/a0h7sAqON67nO/giphy.gif' />")
    elif id < NUMBER:
        return ("Your guess is too small "
                "<br><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExem9nbjFncmY2bWc5dWdkZTlkdnFwaTBpeDRxMzF5MWlsYnl2Z3l5MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/YYht2UTV41u1vxHTss/giphy.gif' />")
    else:
        return ("Your guess is too large "
                "<br><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExazhsMXE0eXBvNHNmOWs5aGtkYWh3M295bGZ6emlyZXIydjlrYXoyZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/26FKWtP1wjGdrLetG/giphy.gif' />")

if __name__ == "__main__":
    app.run(debug=True)
