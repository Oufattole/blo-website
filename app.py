from flask import Flask, render_template

app = Flask(__name__)

@app.route('/buttons.html')
def buttons():
    return render_template('buttons.html')

@app.route('/utilities-border.html')
def utilities_border():
    return render_template('utilities-border.html')

@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forgot-password.html')
def forgot_password():
    return render_template('forgot-password.html')

@app.route('/utilities-color.html')
def utilities_color():
    return render_template('utilities-color.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.errorhandler(404)
def four_zero_four(e):
    return render_template('404.html'), 404

@app.route('/login.html')
def ogin():
    return render_template('login.html')

@app.route('/blank.html')
def blank():
    return render_template('blank.html')

@app.route('/charts.html')
def charts():
    return render_template('charts.html')

@app.route('/utilities-other.html')
def utilities_other():
    return render_template('utilities-other.html')

@app.route('/tables.html')
def ables():
    return render_template('tables.html')

@app.route('/cards.html')
def cards():
    return render_template('cards.html')

@app.route('/utilities-animation.html')
def utilities_animation():
    return render_template('utilities-animation.html')

@app.route('/teams.html')
def teams():
    return render_template('teams.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()