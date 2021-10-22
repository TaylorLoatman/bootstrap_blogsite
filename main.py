from flask import Flask, render_template
import requests
from pprint import pprint

app = Flask(__name__)

# pprint(all_post)
all_post = requests.get(url='https://api.npoint.io/d30c480322a8d2311384').json()

@app.route('/')
def get_home():
    return render_template('index.html', blog_post=all_post)


@app.route('/about')
def get_about():
    return render_template('about.html')


@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    return render_template('post.html', blog_id=blog_id, blog_post=all_post)


@app.route('/contact')
def get_contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
