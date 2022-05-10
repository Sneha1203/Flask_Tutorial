from flask import Flask
import views

app = Flask(__name__)


app.add_url_rule('/', 'index', views.index, methods=['GET', 'POST'])   # ('url', 'html_file', 'view.function_name()')


if __name__ == "__main__":
    app.run(debug=True)