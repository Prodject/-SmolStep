from views import home, routes, map
from flask import Flask

app = Flask(__name__)

app.add_url_rule('/home/', view_func=home, methods=['GET', 'POST'])
app.add_url_rule('/route/', view_func=routes, methods=['GET', 'POST'])
app.add_url_rule('/map/', view_func=map, methods=['GET', 'POST'])
app.add_url_rule('/contact/', view_func=map, methods=['GET', 'POST'])
app.add_url_rule('/report/', view_func=map, methods=['GET', 'POST'])


def main():
    app.run('127.0.0.1', 7000, debug=True)


if __name__ == '__main__':
    main()