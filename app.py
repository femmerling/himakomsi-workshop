from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

app.secret_key = "S0m3Secretkey$"

def write_to_file(stub, data):
    with open("static/{}.txt".format(stub), "w") as f:
        f.write(data)

def read_from_file(stub):
    with open("static/{}.txt".format(stub)) as f:
        return f.readline()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/article/<stub>')
def read_article(stub):
    content = read_from_file(stub)
    return render_template(
        'article.html',
        title=stub,
        content=content)

@app.route('/article/<stub>/json')
def read_json_article(stub):
    content = read_from_file(stub)
    return dict(title=stub, content=content)

@app.route('/article', methods=["GET", "POST"])
def post_article():
    if request.method == "GET":
        return render_template('post_article.html')
    elif request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        print(title)
        print(content)
        write_to_file(title, content)
        return render_template(
                'article.html',
                title=title,
                content=content)


if __name__ == '__main__':
    app.run(port=8000, debug=True)