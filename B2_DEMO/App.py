from flask import Flask, render_template, redirect, url_for

app = Flask(__name__,
            template_folder='client/templates')

names = ['Fernando', 'Febronia', 'Tiffy', 'Ajun', 'Biju']

@app.route("/")
def hello():
    return render_template('Index.html')

@app.route("/user")
def user():
    return render_template('User.html', users=names)

@app.route("/employee/<name1>")
def employee(name1):
    if name1 == "admin":
        return redirect(url_for('hello'))
    else:
        return redirect(url_for('user', name=name1))


if __name__ == '__main__':
    app.run(debug=True)