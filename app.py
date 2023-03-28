from Flask import flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>My first app</h1>"

if __name__ == '__main__':
    app.run()