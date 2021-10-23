from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)
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


@app.route('/form-entry', methods=['POST'])
def receive_data():
    name = request.form['user']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    my_email = "tloatmancodes@gmail.com"
    password = 'Peyton030%'

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tloatman77@yahoo.com",
            msg=f"Subject:New Message from {name}\n\nEmail: {email}\nNumber: {phone}\nMessage: {message}"
            )
    return render_template('form_entry.html')


if __name__ == "__main__":
    app.run(debug=True)
