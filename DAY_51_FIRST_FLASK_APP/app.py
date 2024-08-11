from flask import Flask
import random
import time
# app = Flask(__name__)

class User :
    def __init__(self,name) :
        self.name = name
        self.login = False



def check_login(func) :
    def wrapper(*args, **kwargs) :
        if args[0].login == True:
            func(args[0])
        else :
            print("You are not logged in")
    return wrapper

@check_login
def create_blog_post(user) :
    print(f"Some logic to create a blog post {user.name}")


# @check_login
new = User("saad")
new.login = True
create_blog_post(new)



# def decorate_make_bold(func):
#     def wrapper():
#        return f"<b>{func()}</b>"  
#     return wrapper

# def decorate_make_emphasis(func):
#     def wrapper():
#        return f"<em>{func()}</em>"
#     return wrapper

# def decorate_make_underlined(func) :
#     def wrapper():
#        return f"<u>{func()}</u>"
#     return wrapper




# @app.route("/")
# @decorate_make_bold
# @decorate_make_underlined
# @decorate_make_emphasis
# def hello_world():
#     return f"Saad"
# if __name__ == "__main__":
#     app.run(debug=True)





