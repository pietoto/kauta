from flask import Flask, render_template

app = Flask(__name__)


@app.route('/test/<sex>/<year>')
def training_1(sex, year):
    return render_template('table.html', gender=sex, old=int(year))


if __name__ == '__main__':
    sex = ''
    year = ''
    app.run(port=8080, host='127.0.0.1')
