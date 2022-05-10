# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "This is home page"


# @app.route('/<name>')
# def variable(name):
#     return "This is variable: {}".format(name)


# @app.route('/blog/<int:blogid>')
# def blog(blogid):
#     return "The blog ID is: {}".format(blogid)

# @app.route('/weight/<float:w>')
# def weight(w):
#     return "WEIGHT: %s"%w


# if __name__ == "__main__":
#     app.run(debug=True)