from flask import Flask, render_template
import requests


app = Flask(__name__)




@app.route('/')
def home():
    all_posts = requests.get("https://api.npoint.io/4af156202f984d3464c3").json()
    return render_template("index.html", posts=all_posts)


@app.route('/blog/<id>')
def get_blog(id):
    all_posts = requests.get("https://api.npoint.io/4af156202f984d3464c3").json()
    return render_template("post.html", posts=all_posts, id=int(id))


if __name__ == "__main__":
    app.run(debug=True)
